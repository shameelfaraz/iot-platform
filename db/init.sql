CREATE TABLE IF NOT EXISTS sensor_readings (
    id SERIAL PRIMARY KEY,
    sensor_id TEXT,
    temperature REAL,
    humidity REAL,
    timestamp TIMESTAMP
);
