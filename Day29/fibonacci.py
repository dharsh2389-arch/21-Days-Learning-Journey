n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

'''Output
Enter number of terms: 15
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
'''
