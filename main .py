# for i in range (2,11,2):
#     print(i)


# no=int(input("enter no for table"))
# for i in range (1,11):
#     print(no,"x",i,"=",no*i)

# a=sum(range(1,11))
# print(a)
n=int(input("enter number of rows"))

for i in range(0,n):
    for j in range(0,i+1):
        print ("*", end=" ")
    print("\n")