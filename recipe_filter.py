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

        ingredient_list = []
        for ing in details.get("ingredients", []):
            ingredient_list.append(ing.lower())

        has_avoid = False
        for ingredient in profile["avoid_ingredients"]:
            if ingredient in ingredient_list:
                has_avoid = True
                break
        if has_avoid:
            continue

        if profile["include_ingredients"]:
            has_preferred = False
            for preferred in profile["include_ingredients"]:
                if preferred in ingredient_list:
                    has_preferred = True
                    break
            if not has_preferred:
                continue

        filtered.append((recipe_name, details))

    return filtered
