from cusorder import customer,order

cus = customer.customer("Jame","Nontaburi")
ord = order.Order("15-06-2022","packed")

print(f'Order of {cus.cus_name} in {cus.address} on {ord.date} is {ord.status}')