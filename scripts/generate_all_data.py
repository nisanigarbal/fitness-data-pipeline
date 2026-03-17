import os

scripts = [
    "generate_data.py",
    "generate_foods.py",
    "generate_meals.py",
    "generate_workouts.py",
    "generate_water_logs.py"
]

for script in scripts:
    print(f"Running {script}...")
    os.system(f"python {script}")

print("All datasets generated!")