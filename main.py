MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def report():
    """Prints the current status of resources."""
    for resource, amount in resources.items():
        unit = "ml" if resource != "money" else "$"
        print(f"{resource.capitalize()}: {amount}{unit}")


def is_resource_sufficient(choice):
    """Checks if there are enough resources to make the selected drink."""
    for ingredient, amount in MENU[choice]['ingredients'].items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Processes the coins inserted by the user and returns the total amount.
    """
    print("Please insert coins.")
    total = (
        int(input("How many quarters? ")) * 0.25 +
        int(input("How many dimes? ")) * 0.10 +
        int(input("How many nickles? ")) * 0.05 +
        int(input("How many pennies? ")) * 0.01
    )
    return round(total, 2)


def check_transaction(choice, payment):
    """Checks if the payment is sufficient and updates the resources if
    successful."""
    cost = MENU[choice]['cost']
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif payment > cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
    resources['money'] += cost
    return True


def make_coffee(choice):
    """Deducts the required ingredients from the resources and serves the
    coffee."""
    for ingredient, amount in MENU[choice]['ingredients'].items():
        resources[ingredient] -= amount
    print(f"Here is your {choice}. Enjoy!")


def coffee_machine():
    """Main function to run the coffee machine program."""
    while True:
        choice = input("What would you"
                       "like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif choice == "report":
            report()
        elif choice in MENU:
            if is_resource_sufficient(choice):
                payment = process_coins()
                if check_transaction(choice, payment):
                    make_coffee(choice)
        else:
            print("Invalid selection. Please choose espresso, latte,"
                  "or cappuccino.")


# Run the coffee machine program
coffee_machine()
