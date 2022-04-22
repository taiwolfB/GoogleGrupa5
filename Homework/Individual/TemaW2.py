list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print("Sorted Asc")
sortedListAsc = list.copy()
sortedListAsc.sort()
print(sortedListAsc)

print("Sorted desc")
sortedListDsc = list.copy()
sortedListDsc.sort(reverse=True)
print(sortedListDsc)

print("Numbers at even positions from list")
print(list[::2])

print("Numbers at odd positions from list")
print(list[1::2])

print("Numbers at  positions multiples of 3 from list")
print(list[::3])
