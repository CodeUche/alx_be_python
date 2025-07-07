class OutOfFruitError(Exception):
    
    def __init__(self, fruit, quantity):
        self.fruit = fruit
        self.quantity = quantity

    def __str__(self):
        return f"You attempted to order {self.quantity} {self.fruit}(s). {self.fruit} is currently out of stock."

fruit_inventory = {
    "apple": 4,
    "kiwi": 5,
    "orange": 3,
    "pear": 7,
    "guava": 2,
    "banana": 0
}

# Lets testing our custom exception

def purchase_fruit(item, quantity):
        try:
            if fruit_inventory[item] == 0:
                raise OutOfFruitError(item, quantity)
            else:
                print(f"You have successfully purchased {quantity} {item}(s)")
                fruit_inventory[item] -= quantity

        except KeyError:
            print(f"Sorry {item} does not exist in our inventory.")
            
        
try:

    purchase_fruit("kiwi", 3)
    purchase_fruit("orange", 1)
    purchase_fruit("pawpaw", 2)
    purchase_fruit("banana", 2)

except OutOfFruitError as e:
    print(e)

finally:
    print("Transaction is completed!")