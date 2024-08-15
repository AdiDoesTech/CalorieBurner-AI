
# Food scanner basically scans what food you ate and gives information;
# Gives the nutrients information and is it good for your health or not.


bad_foods = {
    "Double cheeseburgers": {
        "calories": 800,
        "nutrients": "Protein: 37g, Carbs: 44g, Fat: 47g",
        "fun_facts": "Double cheeseburgers often contain more calories than a daily recommended amount for an average adult."
    },
    "Fried chicken (1 piece)": {
        "calories": 400,
        "nutrients": "Protein: 18g, Carbs: 10g, Fat: 24g",
        "fun_facts": "Fried chicken is a popular comfort food, but its high fat content can contribute to health issues if eaten frequently."
    },
    "French fries (medium)": {
        "calories": 365,
        "nutrients": "Protein: 4g, Carbs: 63g, Fat: 17g",
        "fun_facts": "French fries are known for their high oil content and are often associated with increased risk of heart disease."
    },
    "Hot dogs": {
        "calories": 150,
        "nutrients": "Protein: 5g, Carbs: 2g, Fat: 13g",
        "fun_facts": "Hot dogs are a popular fast food, but they are often high in sodium and preservatives."
    },
    "Pizza (slice with heavy toppings)": {
        "calories": 300,
        "nutrients": "Protein: 12g, Carbs: 36g, Fat: 14g",
        "fun_facts": "Pizza with heavy toppings can contain more calories than a full meal due to added cheese and meats."
    },
    "Potato chips (1 oz)": {
        "calories": 150,
        "nutrients": "Protein: 2g, Carbs: 15g, Fat: 10g",
        "fun_facts": "Potato chips are often fried in oil, which increases their calorie and fat content."
    },
    "Doritos (1 oz)": {
        "calories": 140,
        "nutrients": "Protein: 2g, Carbs: 18g, Fat: 7g",
        "fun_facts": "Doritos are a popular snack with a distinctive flavor, but they are also high in sodium and artificial ingredients."
    },
    "Pretzels (1 oz)": {
        "calories": 110,
        "nutrients": "Protein: 2g, Carbs: 23g, Fat: 1g",
        "fun_facts": "Pretzels are a lower-fat snack option but are still high in sodium."
    },
    "Cheese puffs (1 oz)": {
        "calories": 150,
        "nutrients": "Protein: 2g, Carbs: 15g, Fat: 9g",
        "fun_facts": "Cheese puffs are often made from processed cheese and can be high in artificial flavorings."
    },
    "Flavored popcorn (1 oz)": {
        "calories": 100,
        "nutrients": "Protein: 2g, Carbs: 15g, Fat: 5g",
        "fun_facts": "Flavored popcorn is typically high in sugars and fats, depending on the flavoring used."
    },
    "Donuts (1)": {
        "calories": 250,
        "nutrients": "Protein: 3g, Carbs: 30g, Fat: 14g",
        "fun_facts": "Donuts are a sweet treat with high sugar and fat content, often leading to weight gain if consumed in excess."
    },
    "Pastries (1)": {
        "calories": 300,
        "nutrients": "Protein: 4g, Carbs: 36g, Fat: 16g",
        "fun_facts": "Pastries are often made with refined flour and butter, contributing to high calorie and fat content."
    },
    "Candy (chocolate bar)": {
        "calories": 230,
        "nutrients": "Protein: 2g, Carbs: 28g, Fat: 12g",
        "fun_facts": "Chocolate bars can provide a quick energy boost but are also high in sugar and saturated fats."
    },
    "Ice cream (1 cup)": {
        "calories": 250,
        "nutrients": "Protein: 4g, Carbs: 31g, Fat: 14g",
        "fun_facts": "Ice cream is a popular dessert that can be high in both sugar and fat."
    },
    "Sugary cereals (1 cup)": {
        "calories": 150,
        "nutrients": "Protein: 2g, Carbs: 35g, Fat: 1g",
        "fun_facts": "Sugary cereals are often high in sugar and low in protein, making them less nutritious."
    },
    "Soda (12 oz)": {
        "calories": 150,
        "nutrients": "Protein: 0g, Carbs: 39g, Fat: 0g",
        "fun_facts": "Soda is high in sugar and can contribute to weight gain and other health issues."
    },
    "Energy drinks (12 oz)": {
        "calories": 160,
        "nutrients": "Protein: 0g, Carbs: 42g, Fat: 0g",
        "fun_facts": "Energy drinks contain high levels of caffeine and sugar, which can lead to energy crashes."
    },
    "Sweetened iced teas (12 oz)": {
        "calories": 120,
        "nutrients": "Protein: 0g, Carbs: 32g, Fat: 0g",
        "fun_facts": "Sweetened iced tea is often high in sugar, making it a less healthy beverage option."
    },
    "Milkshakes (12 oz)": {
        "calories": 500,
        "nutrients": "Protein: 12g, Carbs: 64g, Fat: 22g",
        "fun_facts": "Milkshakes can be high in calories and sugar, contributing to weight gain if consumed frequently."
    },
    "Commercial fruit juices (12 oz)": {
        "calories": 150,
        "nutrients": "Protein: 1g, Carbs: 36g, Fat: 0g",
        "fun_facts": "Commercial fruit juices often contain added sugars and lack the fiber found in whole fruits."
    },
    "Processed meats (2 oz)": {
        "calories": 200,
        "nutrients": "Protein: 10g, Carbs: 1g, Fat: 17g",
        "fun_facts": "Processed meats are high in sodium and preservatives, which can be detrimental to health."
    },
    "White bread (1 slice)": {
        "calories": 70,
        "nutrients": "Protein: 2g, Carbs: 12g, Fat: 1g",
        "fun_facts": "White bread is made from refined flour, which can lead to rapid spikes in blood sugar levels."
    },
    "Instant noodles (1 cup)": {
        "calories": 200,
        "nutrients": "Protein: 6g, Carbs: 26g, Fat: 8g",
        "fun_facts": "Instant noodles are quick and convenient but are often high in sodium and low in nutrients."
    },
    "Processed cheese products (1 slice)": {
        "calories": 60,
        "nutrients": "Protein: 3g, Carbs: 1g, Fat: 5g",
        "fun_facts": "Processed cheese products often contain additives and preservatives to enhance flavor and shelf life."
    },
    "Frozen meals (1 serving)": {
        "calories": 350,
        "nutrients": "Protein: 15g, Carbs: 45g, Fat: 15g",
        "fun_facts": "Frozen meals are convenient but can be high in sodium and preservatives."
    }
}

def bad_foods_scanner(bad_foods, food_item):
    # Check if the food item is in the bad_foods dictionary
    if food_item in bad_foods:
        # Retrieve the details of the food item
        food_details = print(bad_foods[food_item])  # The food item in bad foods

        # Format the output
        result = (
            f"Food Item: {food_item}\n"
            f"Calories: {food_details['calories']}\n"
            f"Nutrients: {food_details['nutrients']}\n"
            f"Fun Facts: {food_details['fun_facts']}"
        )

        return result
    else:
        # Return a message if the food item is not found
        return "Be better, balance it and mix your diet with healthiness."

# Example usage
Get_food_group = input("What food did you eat today that you would like to scan? :")
print(bad_foods_scanner(bad_foods, Get_food_group))


okay_foods = okay_foods = {
    "Peanut butter (2 tbsp)": {
        "calories": 190,
        "nutrients": "Protein: 8g, Carbs: 6g, Fat: 16g",
        "fun_facts": "Peanut butter is a good source of protein and healthy fats, but it is also calorie-dense."
    },
    "Cheese (1 oz)": {
        "calories": 110,
        "nutrients": "Protein: 7g, Carbs: 1g, Fat: 9g",
        "fun_facts": "Cheese provides a good amount of calcium and protein but is also high in fat."
    },
    "Granola bars (1 bar)": {
        "calories": 200,
        "nutrients": "Protein: 4g, Carbs: 30g, Fat: 8g",
        "fun_facts": "Granola bars can be a convenient snack, but be cautious of added sugars."
    },
    "Regular yogurt (6 oz)": {
        "calories": 150,
        "nutrients": "Protein: 6g, Carbs: 20g, Fat: 3g",
        "fun_facts": "Yogurt is a good source of protein and calcium, but watch out for added sugars."
    },
    "Whole wheat bread (1 slice)": {
        "calories": 80,
        "nutrients": "Protein: 4g, Carbs: 14g, Fat: 1g",
        "fun_facts": "Whole wheat bread is higher in fiber compared to white bread."
    },
    "Canned soup (1 cup)": {
        "calories": 150,
        "nutrients": "Protein: 6g, Carbs: 20g, Fat: 4g",
        "fun_facts": "Canned soup can be high in sodium, so check labels for sodium content."
    },
    "Frozen vegetables (1 cup)": {
        "calories": 100,
        "nutrients": "Protein: 3g, Carbs: 20g, Fat: 0g",
        "fun_facts": "Frozen vegetables are a convenient way to get your daily servings of veggies."
    },
    "Bagels (1)": {
        "calories": 250,
        "nutrients": "Protein: 10g, Carbs: 50g, Fat: 1g",
        "fun_facts": "Bagels are high in carbohydrates and can be quite filling."
    },
    "Rice cakes (1)": {
        "calories": 35,
        "nutrients": "Protein: 1g, Carbs: 7g, Fat: 0g",
        "fun_facts": "Rice cakes are low in calories but can be a bit bland on their own."
    },
    "Lightly salted nuts (1 oz)": {
        "calories": 170,
        "nutrients": "Protein: 6g, Carbs: 6g, Fat: 15g",
        "fun_facts": "Nuts are a good source of healthy fats and protein but can be high in calories."
    },
    "Low-fat snacks (1 serving)": {
        "calories": 100,
        "nutrients": "Varies by snack",
        "fun_facts": "Low-fat snacks can help manage calorie intake, but check for added sugars."
    },
    "Diet sodas (12 oz)": {
        "calories": 0,
        "nutrients": "Protein: 0g, Carbs: 0g, Fat: 0g",
        "fun_facts": "Diet sodas have no calories but may contain artificial sweeteners."
    },
    "Flavored water (without added sugars) (12 oz)": {
        "calories": 0,
        "nutrients": "Protein: 0g, Carbs: 0g, Fat: 0g",
        "fun_facts": "Flavored water can be a good alternative to sugary beverages if no added sugars are present."
    },
    "Whole grain crackers (5 pieces)": {
        "calories": 70,
        "nutrients": "Protein: 1g, Carbs: 11g, Fat: 2g",
        "fun_facts": "Whole grain crackers are a source of fiber and can be a healthier snack option."
    },
    "Certain protein bars (1 bar)": {
        "calories": 200,
        "nutrients": "Protein: 15g, Carbs: 20g, Fat: 7g",
        "fun_facts": "Protein bars can be a convenient way to boost protein intake, but check for added sugars."
    }
}


def okay_foods_scanner(okay_foods, food_item):
    #  Check if the food item is in the okay foods dictionary
    if food_item in okay_foods:
        # Get details of the food item
        food_details = okay_foods[food_item] # The food item in okay foods

        # Format the response
        result = (
            f"Foood Item: {food_item}\n"
            f"Calories: {food_details['calories']}\n"
            f"Nutrients: {food_details['nutrients']}\n"
            f"Fun Facts: {food_details['fun_facts']}"
        )

        return result
    else:
        # Return a message if the food item is not found
        return "Be better, balance it and mix your diet with healthiness."


healthy_foods = healthy_foods = {
    "Apples (1 medium)": {
        "calories": 95,
        "nutrients": "Protein: 0g, Carbs: 25g, Fat: 0g",
        "fun_facts": "Apples are high in fiber and vitamin C, making them a great snack for overall health."
    },
    "Bananas (1 medium)": {
        "calories": 105,
        "nutrients": "Protein: 1g, Carbs: 27g, Fat: 0g",
        "fun_facts": "Bananas are rich in potassium and vitamin B6, and can help with digestion."
    },
    "Oranges (1 medium)": {
        "calories": 62,
        "nutrients": "Protein: 1g, Carbs: 15g, Fat: 0g",
        "fun_facts": "Oranges are an excellent source of vitamin C and antioxidants."
    },
    "Berries (1 cup)": {
        "calories": 60,
        "nutrients": "Protein: 1g, Carbs: 15g, Fat: 0g",
        "fun_facts": "Berries are high in antioxidants and vitamins, and can help improve heart health."
    },
    "Grapes (1 cup)": {
        "calories": 60,
        "nutrients": "Protein: 0g, Carbs: 16g, Fat: 0g",
        "fun_facts": "Grapes contain antioxidants and are beneficial for heart health and hydration."
    },
    "Spinach (1 cup)": {
        "calories": 7,
        "nutrients": "Protein: 1g, Carbs: 1g, Fat: 0g",
        "fun_facts": "Spinach is rich in iron and vitamins A and C, making it great for overall health."
    },
    "Broccoli (1 cup)": {
        "calories": 55,
        "nutrients": "Protein: 4g, Carbs: 11g, Fat: 1g",
        "fun_facts": "Broccoli is high in vitamins K and C, fiber, and antioxidants."
    },
    "Carrots (1 cup)": {
        "calories": 50,
        "nutrients": "Protein: 1g, Carbs: 12g, Fat: 0g",
        "fun_facts": "Carrots are high in beta-carotene, which is converted to vitamin A in the body."
    },
    "Bell peppers (1 medium)": {
        "calories": 30,
        "nutrients": "Protein: 1g, Carbs: 7g, Fat: 0g",
        "fun_facts": "Bell peppers are rich in vitamins A and C and add a crunchy texture to meals."
    },
    "Kale (1 cup)": {
        "calories": 33,
        "nutrients": "Protein: 2g, Carbs: 7g, Fat: 1g",
        "fun_facts": "Kale is a nutrient-dense leafy green high in vitamins A, C, and K."
    },
    "Chicken breast (3 oz)": {
        "calories": 140,
        "nutrients": "Protein: 26g, Carbs: 0g, Fat: 3g",
        "fun_facts": "Chicken breast is a lean source of protein and is low in fat."
    },
    "Salmon (3 oz)": {
        "calories": 180,
        "nutrients": "Protein: 22g, Carbs: 0g, Fat: 10g",
        "fun_facts": "Salmon is rich in omega-3 fatty acids, which are good for heart health."
    },
    "Tofu (1/2 cup)": {
        "calories": 94,
        "nutrients": "Protein: 10g, Carbs: 3g, Fat: 5g",
        "fun_facts": "Tofu is a versatile plant-based protein and is a good source of iron and calcium."
    },
    "Legumes (1 cup lentils)": {
        "calories": 230,
        "nutrients": "Protein: 18g, Carbs: 40g, Fat: 1g",
        "fun_facts": "Lentils are high in protein and fiber, making them a great plant-based protein source."
    },
    "Eggs (1 large)": {
        "calories": 70,
        "nutrients": "Protein: 6g, Carbs: 1g, Fat: 5g",
        "fun_facts": "Eggs are a complete protein source and provide essential vitamins and minerals."
    },
    "Quinoa (1 cup cooked)": {
        "calories": 220,
        "nutrients": "Protein: 8g, Carbs: 39g, Fat: 4g",
        "fun_facts": "Quinoa is a complete protein and is rich in fiber and essential amino acids."
    },
    "Brown rice (1 cup cooked)": {
        "calories": 215,
        "nutrients": "Protein: 5g, Carbs: 45g, Fat: 1g",
        "fun_facts": "Brown rice is a whole grain and provides more nutrients and fiber than white rice."
    },
    "Oats (1/2 cup dry)": {
        "calories": 150,
        "nutrients": "Protein: 5g, Carbs: 27g, Fat: 3g",
        "fun_facts": "Oats are high in fiber and can help lower cholesterol levels."
    },
    "Whole grain pasta (1 cup cooked)": {
        "calories": 170,
        "nutrients": "Protein: 7g, Carbs: 35g, Fat: 1g",
        "fun_facts": "Whole grain pasta is higher in fiber and nutrients compared to regular pasta."
    },
    "Barley (1 cup cooked)": {
        "calories": 200,
        "nutrients": "Protein: 4g, Carbs: 44g, Fat: 1g",
        "fun_facts": "Barley is a good source of fiber and can help regulate blood sugar levels."
    },
    "Avocados (1/2 medium)": {
        "calories": 120,
        "nutrients": "Protein: 1g, Carbs: 6g, Fat: 11g",
        "fun_facts": "Avocados are rich in healthy fats and provide a good source of vitamins and minerals."
    },
    "Nuts (1 oz almonds)": {
        "calories": 160,
        "nutrients": "Protein: 6g, Carbs: 6g, Fat: 14g",
        "fun_facts": "Almonds are high in healthy fats, protein, and vitamin E."
    },
    "Seeds (1 oz chia)": {
        "calories": 140,
        "nutrients": "Protein: 4g, Carbs: 12g, Fat: 9g",
        "fun_facts": "Chia seeds are a good source of omega-3 fatty acids, fiber, and protein."
    },
    "Olive oil (1 tbsp)": {
        "calories": 120,
        "nutrients": "Protein: 0g, Carbs: 0g, Fat: 14g",
        "fun_facts": "Olive oil is high in monounsaturated fats and antioxidants, beneficial for heart health."
    },
    "Fatty fish (3 oz salmon)": {
        "calories": 180,
        "nutrients": "Protein: 22g, Carbs: 0g, Fat: 10g",
        "fun_facts": "Fatty fish like salmon are rich in omega-3 fatty acids, which support brain and heart health."
    }
}


def healthy_foods_scanner(healthy_foods, food_item):
    # check if the food item is in the healthy foods dictionary
    if food_item in healthy_foods:
        # get details of the food item
        food_details = healthy_foods[food_item]

        # Format the response
        result = (
            f"Foood Item: {food_item}\n"
            f"Calories: {food_details['calories']}\n"
            f"Nutrients: {food_details['nutrients']}\n"
            f"Fun Facts: {food_details['fun_facts']}"
        )

        return result
    else:
        # Return a message if the food item is not found
        return "Doing very good, keep it up."


