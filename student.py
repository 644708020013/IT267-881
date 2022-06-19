class student:

    def __init__(self,id,name,major,) -> None:
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(F"major: {self.major}")

    def __del__(self):
        print("Object was destroyed")

if __name__=="__main__":
    my_student = student(111,"Jessica","IT")
    my_student.display_detail()

    my_student = student(112,"John","MKT")
    my_student.display_detail()

    my_student = student(113,"James","acc")
    my_student.display_detail()




