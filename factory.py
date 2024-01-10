from abc import ABC, abstractmethod

class PizzaStore(ABC):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

class Pizza(ABC):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []
    
    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print("    " + topping)
    
    def bake(self):
        print("Bake for 25 minutes at 350")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Place pizza in official PizzaStore box")
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        display = "---- " + self.name + " ----\n"
        display += self.dough + "\n"
        display += self.sauce + "\n"
        for topping in self.toppings:
            display += topping + "\n"
        return display

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")

class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Veggie Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Pepper")
    
class NYStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Clam Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Fresh Clams from Long Island Sound")

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Pepper")
    
class ChicagoStyleCheesePizza(Pizza):  
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
    
    def cut(self):
        print("Cutting the pizza into square slices")
    
class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Deep Dish Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Eggplant")
    
    def cut(self):
        print("Cutting the pizza into square slices")
    
class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Clam Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Frozen Clams from Chesapeake Bay")
    
    def cut(self):
        print("Cutting the pizza into square slices")

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Eggplant")
        self.toppings.append("Sliced Pepperoni")
    
    def cut(self):
        print("Cutting the pizza into square slices")

class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "veggie":
            return NYStyleVeggiePizza()
        elif pizza_type == "clam":
            return NYStyleClamPizza()
        elif pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "veggie":
            return ChicagoStyleVeggiePizza()
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return None
        
if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    
    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()}\n")
    
    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.get_name()}\n")
    
    pizza = ny_store.order_pizza("clam")
    print(f"Ethan ordered a {pizza.get_name()}\n")
    
    pizza = chicago_store.order_pizza("clam")
    print(f"Joel ordered a {pizza.get_name()}\n")
    
    pizza = ny_store.order_pizza("pepperoni")
    print(f"Ethan ordered a {pizza.get_name()}\n")
    
    pizza = chicago_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza.get_name()}\n")
    
    pizza = ny_store.order_pizza("veggie")
    print(f"Ethan ordered a {pizza.get_name()}\n")
    
    pizza = chicago_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza.get_name()}\n")