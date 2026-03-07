'''Question
A shop records daily sales amounts in a list.
Write a recursive program to calculate the total sales amount.
Example
Input sales list
[1200, 800, 450, 600]
Output
Total Sales: 3050'''

def total_sales(sales):
    if len(sales) == 0:
        return 0
    return sales[0] + total_sales(sales[1:])
sales = [1200, 800, 450, 600]
print("Total Sales:", total_sales(sales))

'''
Output:
Total Sales: 3050
'''
