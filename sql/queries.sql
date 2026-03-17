-- DAILY CALORIES
SELECT user_id, SUM(calories) AS total_calories
FROM meal_logs
WHERE date = CURRENT_DATE
GROUP BY user_id;

-- WEEKLY CALORIES
SELECT user_id, SUM(calories) AS total_calories
FROM meal_logs
WHERE date >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY user_id;

-- LEADERBOARD (WORKOUT)
SELECT user_id, SUM(calories_burned) AS total_burned
FROM workout_logs
GROUP BY user_id
ORDER BY total_burned DESC;

-- MOST CONSUMED FOOD
SELECT food_id, COUNT(*) AS count
FROM meal_logs
GROUP BY food_id
ORDER BY count DESC;