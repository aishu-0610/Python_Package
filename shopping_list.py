def create_shopping_list(meal_plan):
    all_ingredients = []

    for recipe in meal_plan:
        recipe_name = recipe[0]
        recipe_details = recipe[1]

        if "ingredients" in recipe_details:
            ingredients = recipe_details["ingredients"]
        else:
            ingredients = []

        for ingredient in ingredients:
            all_ingredients.append(ingredient)

    unique_ingredients = []
    for ingredient in all_ingredients:
        if ingredient not in unique_ingredients:
            unique_ingredients.append(ingredient)

    unique_ingredients.sort()
    return unique_ingredients

