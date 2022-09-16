WowVariable=24.99
WowDiscount=0.8
WowTax=1.13
WowFinalPrice=WowVariable*WowDiscount*WowTax

WowFinalPrice = str(round(WowFinalPrice, 2))


print('Initial Price:', WowVariable, 'Discount:', WowDiscount, 'Tax:', WowTax, 'Final Price:', WowFinalPrice)

# for x in range(5,21):
#     print(x)

# for x in range(1, 100, 2):
#     print(x)


# for x in range(75, -1, -1):
#     print(x)

