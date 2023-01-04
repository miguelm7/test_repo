# we use typing to specify the expcted type or agruments
#if whe have an optional argument which we specify the default value,
#typing is not needed because the expected type is it of the default value
#in this case quantity=0 -> int

class Item:
    def __init__(self, name: str, price: float, quantity = 0) -> None:
        # validate received arguments
        assert price>=0, f"Price {price} is not >=0 !"
        assert quantity>=0, f"Quantity {quantity} is not >=0 !"

        #assign attribute values
        self.name = name
        self.price = price
        self.quantity = quantity

        print(f"Created instance: {name}")

    def calculate_amount(self):
        return self.price * self.quantity

        
item1=Item("Phone", 100, 3)
item2=Item("Laptop",1000,2)

print(item1.calculate_amount())
print(item2.calculate_amount())
     
