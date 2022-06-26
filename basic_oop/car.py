class Car:
    brand = "Toyota"

    def __init__(self,model,colour,year,price) -> None:
        self.model = model
        self.colour = colour
        self.year = year 
        self.price = price

    def printCarDetail(self):
        print(f"Brand: {self.brand}")
        print(f"Modl: {self.model}")
        print(F"Colour: {self.colour}")
        print(F":year {self.year}")
        print(F"price: {self.price:,.2f}")

    def __del__(self):
        print("Object was destroyed")

if __name__=="__main__":
    my_car = Car("Cross","white",2022,1500000)
    my_car.printCarDetail()