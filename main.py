import json
from user_input import get_user_preferences
from recipe_filter import filter_recipes
from meal_plan import generate_meal_plan
from shopping_list import create_shopping_list

def load_recipes(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def display_meal_plan(meal_plan):
    print("\nYour Personalized Meal Plan:\n")
    for i, recipe in enumerate(meal_plan, 1):
        recipe_name, recipe_details = recipe
        print(f"Meal {i}: {recipe_name}")
        print(f"Calories: {recipe_details.get('calorie', 'N/A')} kcal")
        print("Ingredients:")
        for ingredient in recipe_details.get('ingredients', []):
            print("-", ingredient)
        print("Steps:")
        for step in recipe_details.get('steps', []):
            print("-", step)
        print("--------------------------------------------------")

def display_shopping_list(shopping_list):
    print("\nGenerated Shopping List:")
    for ingredient in shopping_list:
        print("-", ingredient)

def main():
    recipes = load_recipes('recipes_with_calories.json')
    user_profile = get_user_preferences()
    filtered = filter_recipes(recipes, user_profile)
    meal_plan = generate_meal_plan(filtered)

    if not meal_plan:
        print("\nNo matching recipes found for your preferences.")
    else:
        display_meal_plan(meal_plan)
        shopping_list = create_shopping_list(meal_plan)
        display_shopping_list(shopping_list)

if __name__ == "__main__":
    main()
