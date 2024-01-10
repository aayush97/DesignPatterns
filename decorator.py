from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self):
        self.description = "Unknown Beverage"
    
    def get_description(self):
        return self.description
    
    @abstractmethod
    def cost(self):
        pass

class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass

class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
    
    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"
    
    def cost(self):
        return 0.89

class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"
    
    def cost(self):
        return 0.99
    
class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf Coffee"
    
    def cost(self):
        return 1.05

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + ", Mocha"
    
    def cost(self):
        return 0.20 + self.beverage.cost()

class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + ", Soy"
    
    def cost(self):
        return 0.15 + self.beverage.cost()

class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + ", Whip"
    
    def cost(self):
        return 0.10 + self.beverage.cost()

if __name__ == "__main__":
    beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")
    
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${beverage2.cost()}")
    
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${beverage3.cost()}")
    
    beverage4 = Decaf()
    beverage4 = Soy(beverage4)
    beverage4 = Mocha(beverage4)
    beverage4 = Whip(beverage4)
    print(f"{beverage4.get_description()} ${beverage4.cost()}")

