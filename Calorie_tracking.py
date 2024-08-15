import tkinter as tk

from tkinter import messagebox

bad_foods = {

    "double cheeseburgers": {"calories": 800, "workout": "Running (1.5 hours)"},

    "cheeseburgers": {"calories": 800, "workout": "Running (1.5 hours)"},

    "fried chicken (1 piece)": {"calories": 400, "workout": "Cycling (0.8 hours)"},

    "french fries (medium)": {"calories": 365, "workout": "Swimming (0.5 hours)"},

    "hot dogs": {"calories": 150, "workout": "Walking (0.3 hours)"},

    "pizza (slice with heavy toppings)": {"calories": 300, "workout": "Football (0.6 hours)"},

    "potato chips (1 oz)": {"calories": 150, "workout": "Weightlifting (0.5 hours)"},

    "doritos (1 oz)": {"calories": 140, "workout": "Running (0.2 hours)"},

    "pretzels (1 oz)": {"calories": 110, "workout": "Cycling (0.2 hours)"},

    "cheese puffs (1 oz)": {"calories": 150, "workout": "Swimming (0.2 hours)"},

    "flavored popcorn (1 oz)": {"calories": 100, "workout": "Walking (0.2 hours)"},

    "donuts (1)": {"calories": 250, "workout": "Running (0.5 hours)"},

    "pastries (1)": {"calories": 300, "workout": "Cycling (0.6 hours)"},

    "candy (chocolate bar)": {"calories": 230, "workout": "Swimming (0.3 hours)"},

    "ice cream (1 cup)": {"calories": 250, "workout": "Football (0.5 hours)"},

    "sugary cereals (1 cup)": {"calories": 150, "workout": "Weightlifting (0.3 hours)"},

    "soda (12 oz)": {"calories": 150, "workout": "Running (0.2 hours)"},

    "energy drinks (12 oz)": {"calories": 160, "workout": "Cycling (0.3 hours)"},

    "sweetened iced teas (12 oz)": {"calories": 120, "workout": "Swimming (0.2 hours)"},

    "milkshakes (12 oz)": {"calories": 500, "workout": "Football (1 hour)"},

    "commercial fruit juices (12 oz)": {"calories": 150, "workout": "Weightlifting (0.3 hours)"},

    "processed meats (2 oz)": {"calories": 200, "workout": "Running (0.4 hours)"},

    "white bread (1 slice)": {"calories": 70, "workout": "Cycling (0.1 hours)"},

    "instant noodles (1 cup)": {"calories": 200, "workout": "Swimming (0.3 hours)"},

    "processed cheese products (1 slice)": {"calories": 60, "workout": "Football (0.1 hours)"},

    "frozen meals (1 serving)": {"calories": 350, "workout": "Weightlifting (0.7 hours)"}

}

okay_foods = {

    "peanut butter (2 tbsp)": {"calories": 190, "workout": "Running (0.4 hours)"},

    "cheese (1 oz)": {"calories": 110, "workout": "Cycling (0.2 hours)"},

    "granola bars (1 bar)": {"calories": 200, "workout": "Swimming (0.3 hours)"},

    "regular yogurt (6 oz)": {"calories": 150, "workout": "Football (0.3 hours)"},

    "whole wheat bread (1 slice)": {"calories": 80, "workout": "Weightlifting (0.2 hours)"},

    "canned soup (1 cup)": {"calories": 150, "workout": "Running (0.2 hours)"},

    "frozen vegetables (1 cup)": {"calories": 100, "workout": "Cycling (0.1 hours)"},

    "bagels (1)": {"calories": 250, "workout": "Swimming (0.4 hours)"},

    "rice cakes (1)": {"calories": 35, "workout": "Football (0.1 hours)"},

    "lightly salted nuts (1 oz)": {"calories": 170, "workout": "Weightlifting (0.3 hours)"},

    "low-fat snacks (1 serving)": {"calories": 100, "workout": "Running (0.2 hours)"},

    "diet sodas (12 oz)": {"calories": 0, "workout": "No workout needed"},

    "flavored water (without added sugars) (12 oz)": {"calories": 0, "workout": "No workout needed"},

    "whole grain crackers (5 pieces)": {"calories": 70, "workout": "Cycling (0.1 hours)"},

    "certain protein bars (1 bar)": {"calories": 200, "workout": "Swimming (0.3 hours)"}

}

healthy_foods = {

    "apples (1 medium)": {"calories": 95, "workout": "Running (0.2 hours)"},

    "bananas (1 medium)": {"calories": 105, "workout": "Cycling (0.2 hours)"},

    "oranges (1 medium)": {"calories": 62, "workout": "Swimming (0.1 hours)"},

    "berries (1 cup)": {"calories": 60, "workout": "Football (0.1 hours)"},

    "grapes (1 cup)": {"calories": 60, "workout": "Weightlifting (0.1 hours)"},

    "spinach (1 cup)": {"calories": 7, "workout": "Running (few minutes)"},

    "broccoli (1 cup)": {"calories": 55, "workout": "Cycling (0.1 hours)"},

    "carrots (1 cup)": {"calories": 50, "workout": "Swimming (0.1 hours)"},

    "bell peppers (1 medium)": {"calories": 30, "workout": "Football (few minutes)"},

    "kale (1 cup)": {"calories": 33, "workout": "Weightlifting (few minutes)"},

    "chicken breast (3 oz)": {"calories": 140, "workout": "Running (0.3 hours)"},

    "salmon (3 oz)": {"calories": 180, "workout": "Cycling (0.4 hours)"},

    "tofu (1/2 cup)": {"calories": 94, "workout": "Swimming (0.2 hours)"},

    "legumes (1 cup lentils)": {"calories": 230, "workout": "Football (0.5 hours)"},

    "eggs (1 large)": {"calories": 70, "workout": "Weightlifting (0.1 hours)"},

    "quinoa (1 cup cooked)": {"calories": 220, "workout": "Running (0.4 hours)"},

    "brown rice (1 cup cooked)": {"calories": 215, "workout": "Cycling (0.4 hours)"},

    "oats (1/2 cup dry)": {"calories": 150, "workout": "Swimming (0.3 hours)"},

    "whole grain pasta (1 cup cooked)": {"calories": 170, "workout": "Football (0.4 hours)"},

    "barley (1 cup cooked)": {"calories": 200, "workout": "Weightlifting (0.4 hours)"},

    "avocados (1/2 medium)": {"calories": 120, "workout": "Running (0.3 hours)"},

    "nuts (1 oz)": {"calories": 170, "workout": "Cycling (0.3 hours)"},

    "seeds (1 oz)": {"calories": 160, "workout": "Swimming (0.3 hours)"},

    "olive oil (1 tbsp)": {"calories": 120, "workout": "Football (0.3 hours)"},

    "plain greek yogurt (1 cup)": {"calories": 100, "workout": "Weightlifting (0.2 hours)"},

    "cottage cheese (1/2 cup)": {"calories": 100, "workout": "Running (0.2 hours)"}

}


def track_calories_and_workout():
    usr_food_eaten = entry_food.get().strip().lower()

    calorie_count = 0

    workout_suggestion = "😴 No workout needed"

    category = ""

    if usr_food_eaten in bad_foods:

        calorie_count = bad_foods[usr_food_eaten]["calories"]

        workout_suggestion = bad_foods[usr_food_eaten]["workout"]

        category = "🚫 Bad foods"

    elif usr_food_eaten in okay_foods:

        calorie_count = okay_foods[usr_food_eaten]["calories"]

        workout_suggestion = okay_foods[usr_food_eaten]["workout"]

        category = "⚖️ Okay foods"

    elif usr_food_eaten in healthy_foods:

        calorie_count = healthy_foods[usr_food_eaten]["calories"]

        workout_suggestion = healthy_foods[usr_food_eaten]["workout"]

        category = "✅ Healthy/Good foods"

    else:

        messagebox.showerror("Error", f"🍽️ Food item '{usr_food_eaten}' not found.")

        return

    result_text.set(f"🍴 You ate: {usr_food_eaten.capitalize()}\n"

                    f"📊 Category: {category}\n"

                    f"🔥 Calories: {calorie_count} kcal\n"

                    f"💪 Workout: {workout_suggestion}")


root = tk.Tk()

root.title("BurnerAI Calorie Counter 🔥")

root.geometry("400x350")

root.configure(bg="#1e1e1e")

label_font = ("Helvetica", 12, "bold")

entry_font = ("Helvetica", 12)

welcome_msg = tk.Label(root, text="Welcome to BurnerAI! 👋", font=("Helvetica", 14, "bold"), fg="white", bg="#1e1e1e")

welcome_msg.pack(pady=10)

label_name = tk.Label(root, text="What's your name?", font=label_font, fg="white", bg="#1e1e1e")

label_name.pack()

entry_name = tk.Entry(root, font=entry_font, fg="white", bg="#333", insertbackground="white")

entry_name.pack(pady=5)

label_food = tk.Label(root, text="Enter what you ate today:", font=label_font, fg="white", bg="#1e1e1e")

label_food.pack(pady=10)

entry_food = tk.Entry(root, font=entry_font, fg="white", bg="#333", insertbackground="white")

entry_food.pack(pady=5)

btn_track = tk.Button(root, text="Track Calories 🔍", font=label_font, fg="white", bg="#ff4500",

                      command=track_calories_and_workout)

btn_track.pack(pady=20)

result_text = tk.StringVar()

label_result = tk.Label(root, textvariable=result_text, justify="left", font=label_font, fg="white", bg="#1e1e1e")

label_result.pack(pady=10)

root.mainloop()
