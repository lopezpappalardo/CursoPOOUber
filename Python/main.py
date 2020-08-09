from car      import Car
from account  import Account
from uberPool import UberPool

if __name__ == "__main__":
    car1 = UberPool("GBHX14", Account("witty", "23785121-8"), "Chevrolet", "Sail")
    print(vars(car1))
    print(vars(car1.driver))