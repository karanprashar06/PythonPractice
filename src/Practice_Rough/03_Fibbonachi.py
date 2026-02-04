n = int(input("Enter the number till which you want fibonachi series "))
a = 0
b =1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b