val = input("Enter your message: ") 
array = [char for char in val]
narray = ["||"]
for i in range(len(val)):
    narray += array[i] + "||||"
narray.pop()
narray.pop()
str1 = ""
for ele in narray:  
        str1 += ele
print(str1)