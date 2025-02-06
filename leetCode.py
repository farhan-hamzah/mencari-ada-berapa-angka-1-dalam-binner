# # number of one bits
nums = int(input())
i = 1
result = 0
b = 0
while nums > 0:
    if nums%2 != 0:
        result = result + i
        b += 1
    nums //= 2
    i *= 10
print(b)

