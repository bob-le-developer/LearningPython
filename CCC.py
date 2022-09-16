# x=int(input())
# y=5*x-400
# print(y)
# if y>0:
#     print(1)
# elif y==0:
#     print(0)
# else:
#     print(-1)


# names = []
# bid_amounts = []
# max_index = -1
# max = -20000000000

# num_bids = int(input())

# for i in range(num_bids):
#     names.append(input())
#     bid_amounts.append(int(input()))
#     if bid_amounts[i] > max:
#         max = bid_amounts[i]
#         maxIndex = i

# print(names[maxIndex])

previous = ""
instruction = ""
direction = ""

while True:
    instruction = input()
    if instruction == "99999":
        break
   
    num = instruction[:2]
    sum = int(num[:1]) + int(num[1:])
    if sum == 0:
        direction = previous
    elif sum % 2 == 0:
        previous = "right"
        direction = "right"
    else:
        previous = "left"
        direction = "left"
    
    print(direction, instruction[2:])





