row_one = float(input())
row_two = float(input())
row_three = int(input())
row_four = int(input())
euro = 1.94

price_vegitables = row_one * row_three
price_fruits = row_two * row_four

sum = (price_fruits + price_vegitables) / euro
print(sum)