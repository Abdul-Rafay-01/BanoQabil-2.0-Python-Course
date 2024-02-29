# write a program to print all the integers tthat arent divisible by 2

# for i in range (1,51):
#     if i/2 and i/3 == 1 :
#         print("divisible by 2 and 3")
#     else:
#         print( i) 

# for i in range(1,51):
#     if i%2 == 0 or i%3 ==0 :
#         print()
#     else :  
#         print(i)


# for i in range(1,51):
#     if i%2  and i%3  :
#         print(i)
   
# for i in range(1,51):
#     if i%2 ==0 or i%3 ==0  :
#         print(i)
        
# def add_three_numbers(a,v,f):
#     add = 4+5+6
#     return add 
    
#     n = add_three_numbers(4,5,6)
#     print(n)

# def find_prime(num):
#     for i in range(2,num):
#         if num%i == 0:
#             print(i,"prime")
#     else:
#         print(i,"not prime")
#     return True
 
# num= 3
# prime_numbers = find_prime(num)
# print(prime_numbers)


def find_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        return True
    
print_num = []
for i in range(1,50):
        prime_numbers = find_prime(i)
        if prime_numbers:
            print_num.append(i)

print(print_num)
