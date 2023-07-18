l = float(input())
w = float(input())

long_hall = l * 100
w_hall = (w * 100) - 100
long_hall_real = long_hall // 120
w_hall_real = w_hall // 70

sum = long_hall_real * w_hall_real - 3
print(sum)