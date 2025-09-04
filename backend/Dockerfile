# Use official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt first (to leverage Docker cache)
COPY requirements.txt .  

# Install dependencies (skip if the file is missing)
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy the rest of the backend files
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
