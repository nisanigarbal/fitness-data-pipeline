from faker import Faker
import pandas as pd
import random

fake = Faker()

users = []

for i in range(100):

    user = {
        "user_id": i + 1,
        "name": fake.name(),
        "email": fake.email(),
        "age": random.randint(18,60),
        "gender": random.choice(["Male","Female"]),
        "height_cm": random.randint(150,195),
        "weight_kg": random.randint(50,110),
        "created_at": fake.date_this_year()
    }

    users.append(user)

df = pd.DataFrame(users)
df.to_csv("users.csv", index=False)
