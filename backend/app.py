from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import DictCursor

app = Flask(__name__)

# Database connection function
def connect_db():
    return psycopg2.connect(
        dbname="wsn_data",
        user="    ",
        password="     ",
        host="timescaledb",
        port="5432"
    )

# ✅ Test Route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "WSN API is running!"}), 200

# ✅ Store sensor data
@app.route("/write", methods=["POST"])
def write_data():
    try:
        data = request.get_json()  # Ensure JSON parsing

        # Validate required fields
        if not data or "sensor_id" not in data or "temperature" not in data or "humidity" not in data:
            return jsonify({"error": "Missing required fields: sensor_id, temperature, humidity"}), 400
        
        # Provide a default pressure value if missing
        pressure = data.get("pressure", 1013)

        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO sensor_data (sensor_id, temperature, humidity, pressure, timestamp) VALUES (%s, %s, %s, %s, NOW())",
                    (data["sensor_id"], data["temperature"], data["humidity"], pressure)
                )
                conn.commit()

        return jsonify({"message": "Data stored successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Retrieve sensor data
@app.route("/read", methods=["GET"])
def read_data():
    try:
        sensor_id = request.args.get("sensor_id")
        if not sensor_id:
            return jsonify({"error": "sensor_id is required"}), 400

        try:
            sensor_id = int(sensor_id)  # Ensure sensor_id is an integer
        except ValueError:
            return jsonify({"error": "sensor_id must be an integer"}), 400

        with connect_db() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute("SELECT * FROM sensor_data WHERE sensor_id = %s ORDER BY timestamp DESC LIMIT 10", (sensor_id,))
                records = cursor.fetchall()

        if not records:
            return jsonify({"message": "No data found for the given sensor_id"}), 404

        return jsonify([dict(record) for record in records]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
