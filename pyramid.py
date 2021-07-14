# Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
# e.g. 1)
# input : 2
# output : 1
# 2 , 1
# 1

# e.g. 2)
# input : 4
# output : 1
# 2 , 1
# 1 , 2 , 3
# 4 , 3 , 2 , 1
# 1 , 2 , 3
# 2 , 1
# 1

# e.g. 3)
# input : 5
# output : 1
# 2 , 1
# 1 , 2 , 3
# 4 , 3 , 2 , 1
# 1 , 2 , 3 , 4 , 5
# 4 , 3 , 2 , 1
# 1 , 2 , 3
# 2 , 1
# 1


# Solution:
rows = int(input("Enter the number:"))

for i in range(1, rows+1):
    if(i%2==1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print(" ")
    else:
        for j in range(i,0,-1):
            print(j, end=' ')
        print(" ")
for i in range(rows-1,0, -1):
    if(i%2==1):
        for j in range(1, i+1 ):
            print(j, end=' ')
        print(" ")
    else:
        for j in range(i,0,-1):
             print(j, end=' ')
        print(" ")





