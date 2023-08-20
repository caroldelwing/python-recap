def buy_sell_stock(prices):
    l, r = 0, 1 #initialize two pointers, left is to buy stock, right to sell (first buy then sell)
    n = len(prices)
    max_profit = 0
    for i in range(n-1): #n-1 bc pointer r started at +1
        if prices[r] > prices[l]: #if it is profitable
            profit = prices[r] - prices[l]
            max_profit=max(max_profit, profit) #select the biggest profit
        else: #if its not profitable
            l = r #move the pointer to the r position (because r is smaller, then best to buy)
        r += 1 #increment r and continue the loop
    return max_profit

print(buy_sell_stock([7,1,5,3,6,4]))