

import time
from calorie_tracking import track_calories_and_workout  # Ensure this import is correct
from Food_Scanner import bad_foods_scanner, okay_foods_scanner, healthy_foods_scanner  # Fix spelling to 'scanner'
from BMI_Checker import main


def main():
    print("Welcome to BurnerAI.")
    time.sleep(0.1)

    usr_name = input("Let's get you set up, what's your name? ")
    activity = input(
        f"Greetings {usr_name}, What type of activity will you be participating in? Calorie Tracking, Food Scanner, BMI Calculator: ")

    if activity.lower() == "calorie tracking":
        usr_food_eaten = input("Enter the food item you have eaten: ")
        track_calories_and_workout(usr_food_eaten)

    elif activity.lower() == "food scanner":
        food_type = input("Choose food type to scan (bad, okay, healthy): ").lower()
        if food_type == "bad":
            bad_foods_scanner()
        elif food_type == "okay":
            okay_foods_scanner()
        elif food_type == "healthy":
            healthy_foods_scanner()
        else:
            print("Invalid food type. Please choose 'bad', 'okay', or 'healthy'.")

    elif activity.lower() == "bmi calculator":
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        bmi = main(height, weight)
        category = main(bmi)
        print(f"Your BMI is {bmi:.2f}, which falls under the category: {category}.")

    else:
        print("Invalid activity type. Please choose 'Calorie Tracking', 'Food Scanner', or 'BMI Calculator'.")


