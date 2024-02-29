# with open("file_test.txt" , 'r' ) as f:
#     data = "hello Dear johsr campus"
#     file = f.read()

# print(file)

# with open("file_test.txt" , "w") as f:
#         data = "\t\t\t\hello Dear johar campus\t\t\t\t"
#         file = f.write(data) 
    
# with open("file_test.txt" , "a" ) as f:
#         data = "fdnviufnvokjfen"
#         file= f.write(data)

#         print(file)  
    
    
with open('file_test.txt' , 'r') as read_file:
    file = read_file.read(3)
    print(file)
