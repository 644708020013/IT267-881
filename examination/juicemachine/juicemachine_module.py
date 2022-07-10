from juicemachine_module import Desserts
from juicemachine_module import Drinks

desserts = Desserts()
print(desserts.show_desserts()) 

drinks = Drinks()
print(drinks.show_drinks())
drinks.add_drink('น้ำส้ม')
print(drinks.show_drinks())
drinks.add_drink('น้ำแอปเปิ้ล')
print(drinks.show_drinks())
drinks.add_drink('น้ำแตงโม')
print(drinks.show_drinks())
drinks.add_drink('น้ำสับปะรด')
print(drinks.show_drinks())
