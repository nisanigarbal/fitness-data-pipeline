import pandas as pd

data = {
    "exercise_name": [
        "Running",
        "Cycling",
        "Walking",
        "HIIT",
        "Weight Training",
        "Yoga",
        "Swimming"
    ],
    "muscle_group": [
        "Legs",
        "Legs",
        "Legs",
        "Full Body",
        "Upper Body",
        "Full Body",
        "Full Body"
    ]
}

df = pd.DataFrame(data)

df.to_csv("exercises.csv", index=False)

print("CSV created!")