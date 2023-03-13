# Necessary libraries are imported
import csv
import datetime


# "Pizza" class is defined
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Subclasses of pizza are defined: "Classic Pizza", "Margherita Pizza", "Turkish Pizza", "Dominos Pizza"
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 25.0)


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 20.0)


class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza", 35.0)


class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 30.0)


# Decorator class is defined - class for all sauces
class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()


# Subclasses of Decorator are defined: "Olives", "Mushrooms", "Goat Cheese", "Meat", "Onions", "Corn".
class Olives(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 5.0

    def get_description(self):
        return self.pizza.get_description() + ", Olives"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Mushrooms(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 6.0

    def get_description(self):
        return self.pizza.get_description() + ", Mushrooms"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 7.0

    def get_description(self):
        return self.pizza.get_description() + ", Goat Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 9.5

    def get_description(self):
        return self.pizza.get_description() + ", Meat"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Onions(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 4.5

    def get_description(self):
        return self.pizza.get_description() + ", Onions"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 3.5

    def get_description(self):
        return self.pizza.get_description() + ", Corn"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

# The main function is defined
def main():
    # Printing the menu
    with open("./menu.txt", 'r', encoding="utf-8") as menu_file:
        menu_text = menu_file.read()
        print(menu_text)

    # The user is prompted to select the pizza and the sauce
    pizza = None
    sauce = None
    while pizza is None:
        pizza_input = input("Please select a pizza: ")
        if pizza_input == "1":
            pizza = ClassicPizza()
        elif pizza_input == "2":
            pizza = MargheritaPizza()
        elif pizza_input == "3":
            pizza = TurkishPizza()
        elif pizza_input == "4":
            pizza = DominosPizza()
        else:
            print("Invalid input. Please try again.")

    while sauce is None:
        sauce_input = input("Please select a sauce: ")
        if sauce_input == "11":
            sauce = Olives(pizza)
        elif sauce_input == "12":
            sauce = Mushrooms(pizza)
        elif sauce_input == "13":
            sauce = GoatCheese(pizza)
        elif sauce_input == "14":
            sauce = Meat(pizza)
        elif sauce_input == "15":
            sauce = Onions(pizza)
        elif sauce_input == "16":
            sauce = Corn(pizza)
        else:
            print("Invalid input. Please try again.")

    # The total cost of the pizza is calculated and the order summary is printed out
    total_cost = sauce.get_cost()
    print("Order Summary:")
    print(pizza.get_description())
    print("Total Cost: ", total_cost)


    # The user is prompted for personal information
    name = input("Please enter your name: ")
    id_no = input("Please enter your TC identity number: ")
    cc_no = input("Please enter your credit card number: ")
    cc_ccv = input("Please enter your credit card CVV: ")
    order_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # The order is saved to the database.
    with open("Orders_Database.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([pizza.__class__.__name__, name, id_no, cc_no, cc_ccv, pizza.get_description(), order_time])
        print("Your order information has been saved. Thank you for your order!")

# The main function is called
if __name__ == '__main__':
    main()