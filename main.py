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

        try:
            choice = int(input("\nEnter the meal number (1, 2, etc.) to view the shopping list: "))
            if choice < 1 or choice > len(meal_plan):
                print("\nInvalid choice. Please select a valid meal number.")
            else:
                selected_recipe = meal_plan[choice - 1]
                shopping_list = create_shopping_list([selected_recipe])
                display_shopping_list(shopping_list)
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
