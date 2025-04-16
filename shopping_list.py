import tkinter as tk
from tkinter import ttk, scrolledtext

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

def display_shopping_list_gui(meal_plan, shopping_list):
    def format_meal_plan_text():
        text = ""
        for i, recipe in enumerate(meal_plan, 1):
            recipe_name, recipe_details = recipe
            text += f"Meal {i}: {recipe_name}\n"
            text += f"Calories: {recipe_details.get('calorie', 'N/A')} kcal\n"
            text += "Ingredients:\n"
            for ingredient in recipe_details.get('ingredients', []):
                text += f"  - {ingredient}\n"
            text += "Steps:\n"
            for step in recipe_details.get('steps', []):
                text += f"  - {step}\n"
            text += "-" * 40 + "\n"
        return text

    def format_shopping_list_text():
        return "\n".join(f"- {item}" for item in shopping_list)

    root = tk.Tk()
    root.title("Meal Plan and Shopping List")
    root.geometry("700x600")

    ttk.Label(root, text="Your Personalized Meal Plan").pack()
    meal_text = scrolledtext.ScrolledText(root, height=15, wrap=tk.WORD)
    meal_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)
    meal_text.insert(tk.END, format_meal_plan_text())

    ttk.Label(root, text="Generated Shopping List").pack()
    shopping_text = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD)
    shopping_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)
    shopping_text.insert(tk.END, format_shopping_list_text())

    root.mainloop()
