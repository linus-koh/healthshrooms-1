import pandas as pd
import random

def generate_meal_plan(filename, breakfast_calories, lunch_calories, dinner_calories):
    # Load the data from the CSV file
    food_data = pd.read_csv(filename)

    # Ensure required columns exist
    required_columns = {'FoodItem', 'Category', 'Calories'}
    if not required_columns.issubset(food_data.columns):
        raise ValueError(f"File must contain these columns: {', '.join(required_columns)}")

    # Helper function to filter by category and calories
    def filter_items(category, max_calories):
        filtered = food_data[
            food_data['Category'].str.contains(category, case=False, na=False) & 
            (food_data['Calories'] <= max_calories)
        ]
        print(f"Filtered items for category '{category}' with max {max_calories} calories:\n", filtered)
        return filtered

    # Select breakfast from "Bread"
    def choose_breakfast():
        breakfast_items = filter_items("Bread", breakfast_calories)
        if breakfast_items.empty:
            return "No suitable breakfast found."
        return random.choice(breakfast_items['FoodItem'].values)

    # Select lunch from "Handheld Entrees" with a beverage
    def choose_lunch():
        lunch_items = filter_items("Handheld Entrees", lunch_calories)
        if lunch_items.empty:
            return "No suitable lunch or beverage found."
        lunch_item = random.choice(lunch_items['FoodItem'].values)
        return f"{lunch_item}"

    # Select dinner from "Entrees" with an appetizer
    def choose_dinner():
        dinner_items = filter_items("Entrees", dinner_calories)
        if dinner_items.empty:
            return "No suitable dinner or appetizer found."
        dinner_item = random.choice(dinner_items['FoodItem'].values)
        return f"{dinner_item}"

    # Generate the meal plan
    meal_plan = {
        "Breakfast": choose_breakfast(),
        "Lunch": choose_lunch(),
        "Dinner": choose_dinner(),
        "Total Calories": round(breakfast_calories + lunch_calories + dinner_calories,2)
    }
    return meal_plan

