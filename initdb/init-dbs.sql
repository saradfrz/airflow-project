-- Create Airflow database and user
CREATE DATABASE airflow;
CREATE USER airflow WITH ENCRYPTED PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

-- Create Superset database and user
CREATE DATABASE superset;
CREATE USER superset WITH ENCRYPTED PASSWORD 'superset';
GRANT ALL PRIVILEGES ON DATABASE superset TO superset;
