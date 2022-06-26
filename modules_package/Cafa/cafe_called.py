#วิธีที่1 
from cafe_module import Dessrets
from cafe_module import Drinks

#วิธีที่2
#from cafe_module import Desserts, Drinks

desserts = Dessrets()
print(desserts.show_desserts())

drinks = Drinks()
print(drinks.show_drinks())

drinks.add_drink('สมูทตี้')
print(drinks.show_drinks())

drinks.add_drink('กาแฟ')
print(drinks.show_drinks())

drinks.add_drink('น้ำผลไม้')
print(drinks.show_drinks())


