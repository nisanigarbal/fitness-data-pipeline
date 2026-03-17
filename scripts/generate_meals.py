import pandas as pd
import random
from faker import Faker

fake = Faker()

meal_logs = []

for i in range(500):

    meal = {
        "user_id": random.randint(1,100),
        "food_id": random.randint(1,10),
        "quantity": random.randint(1,3),
        "date": fake.date_this_year()
    }

    meal_logs.append(meal)

df = pd.DataFrame(meal_logs)

df.to_csv("meal_logs.csv", index=False)

print("Meal logs CSV created!")