import pandas as pd
import random
from faker import Faker

fake = Faker()

water_logs = []

for i in range(300):

    log = {
        "water_id": i + 1,
        "user_id": random.randint(1,100),
        "liters": round(random.uniform(0.5,3.5),1),
        "date": fake.date_this_year()
    }

    water_logs.append(log)

df = pd.DataFrame(water_logs)

df.to_csv("water_logs.csv", index=False)