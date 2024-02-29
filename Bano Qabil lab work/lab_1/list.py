num = int(input("Enter the number :"))

even_list=[]
odd_list=[]
for i in range(1,num+1):
    if i%2 == 0 :
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Even list: {even_list}")
print(f"odd list: {odd_list}")            













# import math
# sqrt= math.sqrt(4)

# print (sqrt)
