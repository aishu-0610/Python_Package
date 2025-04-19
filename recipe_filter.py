def filter_recipes(data, profile):
    max_calories = {
        "weight_loss": 350,
        "muscle_gain": 600,
        "balanced": 450
    }

    allowed_calories = max_calories.get(profile["health_goal"], 450)
    filtered = []

    recipe_list = data.get(profile["diet"], {})

    for recipe_name in recipe_list:
        details = recipe_list[recipe_name]

        recipe_calories = details.get("calorie", 0)
        if recipe_calories > allowed_calories:
            continue

        if profile["max_cooking_time"] is not None:
            recipe_time = details.get("cooking_time", 9999)
            if recipe_time > profile["max_cooking_time"]:
                continue

        ingredient_list = [ing.lower() for ing in details.get("ingredients", [])]
        if any(ingredient in ingredient_list for ingredient in profile["avoid_ingredients"]):
            continue

        if profile["include_ingredients"]:
            if not any(preferred in ingredient_list for preferred in profile["include_ingredients"]):
                continue

        filtered.append((recipe_name, details))

    return filtered
