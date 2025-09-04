CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    sensor_id INT,
    timestamp TIMESTAMPTZ DEFAULT now(),
    temperature FLOAT,
    humidity FLOAT
);

INSERT INTO sensor_data (sensor_id, temperature, humidity) 
VALUES (1, 25.5, 60.2), (2, 26.1, 58.7), (3, 24.8, 62.1);

SELECT * FROM sensor_data;
ALTER TABLE sensor_data ADD COLUMN pressure FLOAT;
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'sensor_data';

UPDATE sensor_data 
SET pressure = 1013  -- You can set a default value
WHERE pressure IS NULL;

-- Verify that all rows have valid values
SELECT * FROM sensor_data;

SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10;

SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10;



