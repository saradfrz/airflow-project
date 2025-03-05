# Airflow Local Setup using Docker

This project provides a local setup of Apache Airflow (version 2.10.5) using Docker Compose. It includes a PostgreSQL container to serve as the metadata database.

## Folder Structure

airflow-docker/ 
├── docker-compose.yaml 
├── README.md 
├── dags/ 
│ └── example_dag.py 
└── plugins/ 
└── init.py

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Running the Project

1. Navigate to the project directory:

   ```bash
   cd airflow-docker