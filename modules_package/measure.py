class Measure:
    def __init__(self) -> None:
        self.reslt = 0
        
    def inch_cm(self,number:float):
        self.reslt = number * 2.54
        return self.reslt
    
    def cm_inch(self,number:float):
        self.result = number / 2.54
        return self.result