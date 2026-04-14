'''
You are given an array where each element is the price of a stock on that day.
Find the maximum profit you can achieve.
You must:
Buy once
Sell once
Sell after buying
'''

def max(prices):
    min=prices[0]
    max=0
    for i in prices:
        if i<min:
            min=i
        profit=i-min
        if profit>max:
            max=profit
    return max
prices = list(map(int, input("Enter prices: ").split()))
print(max(prices))

'''
Output
Enter prices: 7 1 5 3 6 4
5
'''
