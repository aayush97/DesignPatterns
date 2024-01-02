from abc import ABC, abstractmethod

class Duck:
    def __init__(self, name):
        self.name = name
        self.quack_behavior = None
        self.fly_behavior = None

    def perform_quack(self):
        self.quack_behavior.quack()
    
    def perform_fly(self):
        self.fly_behavior.fly()

class MallardDuck(Duck):
    def __init__(self):
        super().__init__("Mallard Duck")

class RedheadDuck(Duck):
    def __init__(self):
        super().__init__("Redhead Duck")
    
class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")
    
class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.quack_behavior = Quack()
    mallard.fly_behavior = FlyWithWings()
    mallard.perform_quack()
    mallard.perform_fly()

    redhead = RedheadDuck()
    redhead.quack_behavior = Squeak()
    redhead.fly_behavior = FlyNoWay()
    redhead.perform_quack()
    redhead.perform_fly()

    redhead.fly_behavior = FlyRocketPowered()
    redhead.perform_fly()
