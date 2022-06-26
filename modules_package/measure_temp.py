from secrets import choice
from measure import Measure

if __name__ == '__main__':
    mobj = Measure()
    choice = input ('Choose menu (1: inch, 2:cm): ')
    number = float(input('Enter number'))
    
    if choice == 1:
        print(f'{number} cm = {mobj.cm_inch(number):.2f} inch')
    elif choice == '2':
        print(f'{number} inch = {mobj.inch_cm(number):.2f} cm')
    else:
        print('Chose wrong menu')
    
    
    #ให้ user เลืกได้ว่าต้องการแปลงค่าเป็น inch หรือ cm 
    #รับค่าตัวเลขจาก user ได้
    
    #print(f'5 cm = {mobj.cm_inch(5):.2f} inch')
    #print(f'18.5 inch = {mobj.inch_cm(18.5):.2f} cm')
    
    
    
