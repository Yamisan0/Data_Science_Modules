CREATE TABLE data_2022_oct (
    created_at TIMESTAMP,
    event_type VARCHAR(255) NOT NULL,
    product_id BIGINT,
    price REAL,
    user_id INTEGER NOT NULL,
    user_session UUID
);