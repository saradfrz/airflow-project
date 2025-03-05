# Airflow Local Setup using Docker

This project provides a local setup of Apache Airflow (version 2.10.5) using Docker Compose. It includes a PostgreSQL container to serve as the metadata database.

## Folder Structure

airflow-docker/ <br>
├── docker-compose.yaml <br>
├── README.md <br>
├── dags/ <br>
│ └── example_dag.py <br>
└── plugins/ <br>
└── init.py<br>

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Running the Project

1. Navigate to the project directory:

   ```bash
   cd airflow-docker