import pandas as pd 
import random

foods = [
    "Chicken Breast",
    "Rice",
    "Egg",
    "Salmon",
    "Broccoli",
    "Oatmeal",
    "Avocado",
    "Banana",
    "Beef",
    "Yogurt"
]

food_data  = []

for i ,food in enumerate(foods):

    item = {
        "food_id": i+1,
        "food_name": food,
        "calories": random.randint(50,400),
        "protein": random.randint(2,40),
        "carbs": random.randint(1,60),
        "fat": random.randint(1,30)
    }

    food_data.append(item)

df = pd.DataFrame(food_data)
df.to_csv("foods.csv", index=False)