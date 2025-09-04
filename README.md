# DockerBased_WSN_Management_System

The Wireless Sensor Network (WSN) Management System is a Docker-based platform designed to collect, store, simulate, and visualize sensor data in real time. It integrates multiple services into a unified system to support IoT, smart city, and research applications. The project leverages containerization for easy deployment and scalability.

# Tech Stack

Flask (Python)           – REST API for sensor data ingestion and retrieval

TimescaleDB (PostgreSQL) – Time-series optimized database

Grafana                  – Real-time visualization dashboards

Node-RED                 – Flow-based tool for sensor simulation and automation

Docker & Docker Compose  – Container orchestration

# Features

REST API for Sensor Data : Store and retrieve temperature, humidity, and pressure readings.

Time-Series Database     : Optimized storage for large-scale sensor data.

Interactive Dashboards   : Real-time visualization using Grafana.

Sensor Simulation        : Node-RED flows for generating and injecting test data.

Containerized Setup      : All components run in isolated containers for easy deployment.

Extensible Architecture  : Easily extendable to support new sensors, analytics, or machine learning modules.

# Installation
Ensure you have Docker and Docker Compose installed on your system. Download the project files from the GitHub repository. Place the wsn_data.sql file, backend folder, Grafana dashboard JSON, and Node-RED flow JSON in the project directory. Configure the docker-compose.yml file as per your environment. Open a terminal in the project folder and run docker-compose up --build to start all services. Once the setup is complete, access the Flask API, Grafana and Node-RED . Please note that additional configuration steps may be required depending on your specific environment.

# Contributing

Contributions are welcome! If you encounter issues or have suggestions, feel free to open an issue or submit a pull request.

# Acknowledgments

Special thanks to the open-source community for providing tools and frameworks that power this project.
