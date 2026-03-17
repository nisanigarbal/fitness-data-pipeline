-- USERS
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    name TEXT,
    email TEXT,
    age INT,
    gender TEXT,
    height_cm INT,
    weight_kg INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- FOODS
CREATE TABLE foods (
    food_id SERIAL PRIMARY KEY,
    name TEXT,
    calories INT
);

-- MEAL LOGS
CREATE TABLE meal_logs (
    id SERIAL PRIMARY KEY,
    user_id UUID,
    food_id INT,
    calories INT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (food_id) REFERENCES foods(food_id)
);

-- WORKOUT LOGS
CREATE TABLE workout_logs (
    id SERIAL PRIMARY KEY,
    user_id UUID,
    calories_burned INT,
    duration_min INT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- WATER LOGS
CREATE TABLE water_logs (
    id SERIAL PRIMARY KEY,
    user_id UUID,
    amount_ml INT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);