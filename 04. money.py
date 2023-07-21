bitcoin = int(input())
chines_juani = float(input())
taxes = float(input()) / 100

bitcoins = bitcoin * 1168
chinas_coins = chines_juani * 0.15 * 1.76

money = (bitcoins + chinas_coins) / 1.95 
commission = money * taxes
total_money = money - commission

print(round(total_money, 2))

