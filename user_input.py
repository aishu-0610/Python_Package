def get_user_preferences():
    print("Welcome to the Healthy Meal Prep Assistant!")

    diet = input("What type of diet do you follow (veg or non-veg)? ").strip().lower()
    while diet not in ['veg', 'non-veg']:
        print("Please choose either 'veg' or 'non-veg'.")
        diet = input("What type of diet do you follow (veg or non-veg)? ").strip().lower()

    health_goal = input("What is your main health goal (weight_loss, muscle_gain, or balanced)? ").strip().lower()
    while health_goal not in ['weight_loss', 'muscle_gain', 'balanced']:
        print("Please enter one of the following options: weight_loss, muscle_gain, or balanced.")
        health_goal = input("What is your main health goal (weight_loss, muscle_gain, or balanced)? ").strip().lower()

    avoid_input = input("Are there any ingredients you want to avoid? (Separate by commas, leave blank if none): ").strip()
    avoid_ingredients = [item.strip().lower() for item in avoid_input.split(",") if item.strip()]

    include_input = input("Are there any ingredients you'd like to include? (Separate by commas, leave blank if none): ").strip()
    include_ingredients = [item.strip().lower() for item in include_input.split(",") if item.strip()]

    while True:
        time_input = input("What’s the maximum cooking time you prefer (in minutes)? Leave blank if no preference: ").strip()
        if time_input == "":
            max_cooking_time = None
            break
        elif time_input.isdigit() and int(time_input) > 0:
            max_cooking_time = int(time_input)
            break
        else:
            print("Please enter a valid number greater than 0, or leave it blank if you have no limit.")

    return {
        "diet": diet,
        "health_goal": health_goal,
        "avoid_ingredients": avoid_ingredients,
        "include_ingredients": include_ingredients,
        "max_cooking_time": max_cooking_time
    }
