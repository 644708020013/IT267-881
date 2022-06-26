class Switch():
    def __init__(self):
        self.switch_status = False

    def turnon(self):
        self.switch_status = True

    def turnoff(self):
        self.switch_status = False

    def show_status(self):
        if (self.switch_status):
            print ("ไฟเปิด")
        else:
            print ("ไฟปิด")
            
    #สร้าง object
sobj = Switch()

if __name__ == "__main__": 
    sobj.show_status()
    sobj.turnon()
    sobj.show_status()
    sobj.turnoff()
    sobj.show_status()
    sobj.turnon()
    sobj.show_status()
    sobj.turnoff()
