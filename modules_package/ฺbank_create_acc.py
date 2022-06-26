from bank.customer import Customer
from bank.account import Account

pual = Customer()
pual.new_customer()
pual_acc = Account()
pual_acc.open_account(pual.name,'Saving','0123-4578',500)

print(pual.cus_info())
print(pual_acc.display_balance())
