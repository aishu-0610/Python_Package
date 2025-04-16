def create_shopping_list(meal_plan):
    all_ingredients = []

    for recipe in meal_plan:
        recipe_name = recipe[0]
        recipe_details = recipe[1]
        ingredients = recipe_details.get("ingredients", [])
        for item in ingredients:
            all_ingredients.append(item)

    unique_ingredients = []
    for item in all_ingredients:
        if item not in unique_ingredients:
            unique_ingredients.append(item)

    unique_ingredients.sort()
    return unique_ingredients
