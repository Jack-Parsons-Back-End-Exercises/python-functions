nums1_to_100 = range(1, 101)

for i in nums1_to_100:
    if i % 7 == 0 and i % 5 == 0:
        print("ChickenMonkey")
    elif i % 5 == 0:
        print("Chicken")
    elif i % 7 == 0:
        print("Monkey")
    else:
        print(i)