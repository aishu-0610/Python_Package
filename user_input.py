def get_user_preferences():
    print("Welcome to the Healthy Meal Prep Assistant!")

    food = input("What type of diet do you follow (veg or non-veg)? ").strip().lower()
    while food not in ['veg', 'non-veg']:
        print("Please choose either 'veg' or 'non-veg'.")
        food = input("What type of diet do you follow (veg or non-veg)? ").strip().lower()

    goal = input("What is your main health goal (weight_loss, muscle_gain, or balanced)? ").strip().lower()
    while goal not in ['weight_loss', 'muscle_gain', 'balanced']:
        print("Please enter one of the following options: weight_loss, muscle_gain, or balanced.")
        goal = input("What is your main health goal (weight_loss, muscle_gain, or balanced)? ").strip().lower()

    skip_input = input("Are there any ingredients you want to avoid? (Separate by commas, leave blank if none): ").strip()
    skip_raw = skip_input.split(",")
    skip_list = []
    for thing in skip_raw:
        thing_clean = thing.strip().lower()
        if thing_clean:
            skip_list.append(thing_clean)

    want_input = input("Are there any ingredients you'd like to include? (Separate by commas, leave blank if none): ").strip()
    want_raw = want_input.split(",")
    want_list = []
    for thing in want_raw:
        thing_clean = thing.strip().lower()
        if thing_clean:
            want_list.append(thing_clean)

    while True:
        time_input = input("What’s the maximum cooking time you prefer (in minutes)? Leave blank if no preference: ").strip()
        if time_input == "":
            max_time = None
            break
        elif time_input.isdigit() and int(time_input) > 0:
            max_time = int(time_input)
            break
        else:
            print("Please enter a valid number greater than 0, or leave it blank if you have no limit.")

    return {
        "diet": food,
        "health_goal": goal,
        "avoid_ingredients": skip_list,
        "include_ingredients": want_list,
        "max_cooking_time": max_time
    }
