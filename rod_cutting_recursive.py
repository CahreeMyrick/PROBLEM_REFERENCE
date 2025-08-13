def rod_cut_recursive(prices, n):

    if n == 0:
        return 0

    best = 0
    for i in range(1, n+1):
        best = max(best, prices[i-1] + rod_cut_recursive(prices, n-i))


    return best

def test():
    prices = [1, 5, 10]
    n = 3
    print(rod_cut_recursive(prices, n))
test()
