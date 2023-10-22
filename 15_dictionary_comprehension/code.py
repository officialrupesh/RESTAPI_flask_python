# square_dictio = dict()

# for num in range(1,11):
#     square_dictio[num] = num * num
#     print(square_dictio)


# rupesh = dict()
# for num in range(0,4):
#     rupesh[num] = num + 1
#     print(rupesh)


# rupesh_comp = {num: num + 1 for num in range(0,4)}

# print(rupesh_comp)


price_in_dollar = {"milk": 1.07,"Vegetable": 1.5, "Coconut": 2}

conversion_rate = 137.5

new_price = { item: value * conversion_rate for(item,value) in price_in_dollar.items() }

print(new_price)


#advantage
#shorten the code
#it maeks our code pythonic