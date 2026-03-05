'''Question
An online store has product prices.
Tasks:
Increase all prices by 18% GST.
Filter products costing more than ₹500.
Combine product names with prices.
Data:
Products: ["Laptop","Mouse","Keyboard","Monitor"]
Prices: [50000,500,1500,8000]'''

products = ["Laptop","Mouse","Keyboard","Monitor"]
prices = [50000,500,1500,8000]
gst_prices = list(map(lambda x: x * 1.18, prices))
expensive = list(filter(lambda x: x > 500, prices))
product_price = dict(zip(products, prices))
print("GST Prices:", gst_prices)
print("Expensive Products:", expensive)
print("Product Price List:", product_price)

'''Output
GST Prices: [59000.0, 590.0, 1770.0, 9440.0]
Expensive Products: [50000, 1500, 8000]
Product Price List: {'Laptop': 50000, 'Mouse': 500, 'Keyboard': 1500, 'Monitor': 8000}
'''
