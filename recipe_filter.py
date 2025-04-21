def filter_recipes(recipes, user):
    calorie_caps = {
        "weight_loss": 350,
        "muscle_gain": 600,
        "balanced": 450
    }

    if "health_goal" in user:
        max_calories = calorie_caps.get(user["health_goal"], 450)
    else:
        max_calories = 450

    if "diet" not in user or user["diet"] not in recipes:
        return []

    diet_recipes = recipes[user["diet"]]
    filtered = []

    for recipe_name in diet_recipes:
        details = diet_recipes[recipe_name]

        if "calorie" not in details:
            continue
        if details["calorie"] > max_calories:
            continue

        if "max_cooking_time" in user and user["max_cooking_time"] is not None:
            if "cooking_time" not in details or details["cooking_time"] > user["max_cooking_time"]:
                continue

        ingredients = []
        if "ingredients" in details:
            for ingredient in details["ingredients"]:
                ingredients.append(ingredient.lower())

        avoid_list = user["avoid_ingredients"] if "avoid_ingredients" in user else []
        found_unwanted = False
        for avoid_item in avoid_list:
            if avoid_item in ingredients:
                found_unwanted = True
                break
        if found_unwanted:
            continue

        preferred_list = user["include_ingredients"] if "include_ingredients" in user else []
        if preferred_list:
            found_preferred = False
            for preferred_item in preferred_list:
                if preferred_item in ingredients:
                    found_preferred = True
                    break
            if not found_preferred:
                continue

        filtered.append((recipe_name, details))

    return filtered
