def get_user_preferences():
    print("Welcome to the Healthy Meal Prep Assistant.")

    diet = input("Please enter your diet type (veg or non-veg): ").strip().lower()
    while diet != 'veg' and diet != 'non-veg':
        print("Invalid choice. Accepted values are 'veg' or 'non-veg'.")
        diet = input("Enter your diet type: ").strip().lower()

    health_goal = input("Enter your health goal (weight_loss, muscle_gain, balanced): ").strip().lower()
    while health_goal not in ['weight_loss', 'muscle_gain', 'balanced']:
        print("Invalid input. Please enter: weight_loss, muscle_gain, or balanced.")
        health_goal = input("Enter your health goal: ").strip().lower()

    avoid_input = input("List any ingredients to avoid (comma-separated). Leave blank if none: ").strip()
    if avoid_input == "":
        avoid_ingredients = []
    else:
        avoid_ingredients = []
        for item in avoid_input.split(","):
            cleaned = item.strip().lower()
            if cleaned != "":
                avoid_ingredients.append(cleaned)

    include_input = input("List any preferred ingredients (comma-separated). Leave blank if none: ").strip()
    if include_input == "":
        include_ingredients = []
    else:
        include_ingredients = []
        for item in include_input.split(","):
            cleaned = item.strip().lower()
            if cleaned != "":
                include_ingredients.append(cleaned)

    return {
        "diet": diet,
        "health_goal": health_goal,
        "avoid_ingredients": avoid_ingredients,
        "include_ingredients": include_ingredients
    }
