eggs = int(input())

carton_size = 12

cartons_filled = eggs // carton_size
rest = eggs % carton_size

print(cartons_filled)
print(rest)
