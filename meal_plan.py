import random as r

def generate_meal_plan(filtered_recipes, number_of_meals=3):
    meal_plan = []

    if not filtered_recipes:
        return meal_plan

    total_available = len(filtered_recipes)
    meals_to_pick = number_of_meals

    if total_available < number_of_meals:
        meals_to_pick = total_available

    index_range = range(total_available)
    random_indexes = r.sample(index_range, meals_to_pick)

    for index in random_indexes:
        meal_plan.append(filtered_recipes[index])

    return meal_plan
