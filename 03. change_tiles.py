n = float(input())
w = float(input())
l = float(input())
m = float(input())
o = float(input())

square_area = n * n
tile = w * l
bench = m * o

area = square_area - bench
area_tile = area / tile
work_time = area_tile * 0.2

print(round(work_time, 2))
print(round(area_tile, 2))