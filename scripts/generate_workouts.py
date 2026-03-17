import pandas as pd
import random
from faker import Faker

fake = Faker()

exercises = [
    "Running",
    "Cycling",
    "Swimming",
    "Weight Training",
    "Yoga",
    "HIIT",
    "Walking"
]

workouts = []

for i in range(400):

    workout = {
        "workout_id": i + 1,
        "user_id": random.randint(1,100),
        "exercise": random.choice(exercises),
        "duration_min": random.randint(10,90),
        "calories_burned": random.randint(80,600),
        "date": fake.date_this_year()
    }

    workouts.append(workout)

df = pd.DataFrame(workouts)

df.to_csv("workout_logs.csv", index=False)