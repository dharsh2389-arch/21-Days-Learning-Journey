'''Create a class Mobile with:
brand
Create 2 objects with different brands.
Print both to show they store separate values.'''

class Mobile:
    def __init__(self, brand):
        self.brand = brand
m1 = Mobile("iqoo")
m2 = Mobile("apple")
print(m1.brand)
print(m2.brand)

'''Output
iqoo
apple'''
