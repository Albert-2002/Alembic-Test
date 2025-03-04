-- Step 1: Create the students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Step 2: Insert sample data
INSERT INTO students (name) VALUES
    ('Alice Johnson'),
    ('Bob Smith'),
    ('Charlie Brown'),
    ('Diana Ross'),
    ('Ethan Hunt');

