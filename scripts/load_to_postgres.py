# cvs okudu, pandas dataframe yaptı, SQLAlchemy ile postgre bağlandı, supabase databse e yüklendi. mini bir data pipeline oluştu.
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
"postgresql://postgres.umsgfymjfbtxloubeojd:Nisabal1234.@aws-1-eu-west-1.pooler.supabase.com:5432/postgres"
)

users = pd.read_csv("users.csv")
foods = pd.read_csv("foods.csv")
meals = pd.read_csv("meal_logs.csv")
workouts = pd.read_csv("workout_logs.csv")
water = pd.read_csv("water_logs.csv")


users.to_sql("users", engine, if_exists="replace", index=False)
foods.to_sql("foods", engine, if_exists="replace", index=False)
meals.to_sql("meal_logs", engine, if_exists="replace", index=False)
workouts.to_sql("workout_logs", engine, if_exists="replace", index=False)
water.to_sql("water_logs", engine, if_exists="replace", index=False)


print("All data loaded into PostgreSQL!")