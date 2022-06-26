from os import mkdir
from empIT import EmpIT

mike = EmpIT('001','Nike',60000)
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()


mike = EmpIT('002','sarawut',18000)
mike.add_skill('admin,system_eng')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()