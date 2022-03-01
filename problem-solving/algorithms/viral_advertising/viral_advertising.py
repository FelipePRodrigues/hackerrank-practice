import math


def viralAdvertising(n):
    liked = 0
    shared = 0
    cumulative = 0

    for idx in range(0, n):
        if not shared:
            shared = 5
        else:
            shared = liked * 3

        liked = math.floor(shared/2)
        cumulative = liked + cumulative

    return cumulative


print(viralAdvertising(1))  # 2
print(viralAdvertising(2))  # 5
print(viralAdvertising(3))  # 9
print(viralAdvertising(4))  # 15
print(viralAdvertising(5))  # 24
