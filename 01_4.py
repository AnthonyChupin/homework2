n = int(input("введите число "))
max =0
while n>0:
    if n%10>max:
        max = n%10
    n=n//10
print (max)
