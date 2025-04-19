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
    avoid_ingredients = [item.strip().lower() for item in avoid_input.split(",") if item.strip() != ""]

    include_input = input("List any preferred ingredients (comma-separated). Leave blank if none: ").strip()
    include_ingredients = [item.strip().lower() for item in include_input.split(",") if item.strip() != ""]

    while True:
        time_input = input("What's the maximum cooking time you prefer (in minutes)? Leave blank for no limit: ").strip()
        if time_input == "":
            max_cooking_time = None
            break
        elif time_input.isdigit() and int(time_input) > 0:
            max_cooking_time = int(time_input)
            break
        else:
            print("Please enter a valid number greater than 0, or leave blank.")

    return {
        "diet": diet,
        "health_goal": health_goal,
        "avoid_ingredients": avoid_ingredients,
        "include_ingredients": include_ingredients,
        "max_cooking_time": max_cooking_time
    }
