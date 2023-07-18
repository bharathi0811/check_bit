def check_bit(n,i):
    num = 1<<i
    ans = num & n
    if ans > 0:
        return 1
    else:
        return 0
integer = int(input("Enter the integer: "))
bit= int(input("Enter the integer bit to check: "))
print(check_bit(integer,bit))