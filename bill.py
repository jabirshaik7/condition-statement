data={
1:{'product':'Rice','price':60},
2:{'product':'Wheat Flour','price':40}, 	  		 
3:{'product':'Sugar','price':80},		 
4:{'product':'Milk','price':25},
5:{'product':'Eggs (12 pcs)','price':70},
6:{'product':'Cooking Oil','price':130},
7:{'product':'Tea Powder','price':90},
8:{'product':'Salt','price':20},
9:{'product':'Bread','price':30},
10:{'product':'Soap','price':25},
}

print('Index'.ljust(7,' '),'Product Name'.ljust(20,' '),'Price'.ljust(10,' '))
for i in data:
    print(str(i).ljust(7,' '),data[i]['product'].ljust(20,' '),str(data[i]['price']).ljust(10,' '))



indexes = list(map(int,input("Enter the indexes: ").split()))


print("Bill".center(30,'-'))
total_bill=0
for i in indexes:
    print(f'{data[i]["product"]} - ${data[i]["price"]}')
    total_bill+= data[i]["price"]

print(f"Your Bill: {total_bill}")

name = input("Enter the name: ")
mobileno = int(input("Enter the mobile no: "))
product_1 = input("Enter the product-1: ")
price_1 = float(input("Enter the product-1 price: "))
product_2 = input("Enter the product-2: ")
price_2 = float(input("Enter the product-2 price: "))
product_3 = input("Enter the product-3: ")
price_3 = float(input("Enter the product-3 price: "))

print(f"{name} your Bill")
print(f"{product_1}: ${price_1}")
print(f"{product_2}: ${price_2}")
print(f"{product_3}: ${price_3}")

total_bill = price_1+price_2+price_3

print(f"Total Bill: {total_bill}")