N = int(input())
# N이 1일 때 = 경우 2
# N이 2일 때 = 경우 4
# N이 3일 때 = 경우 8
# ... N이 n일 때 = 경우 2**n
print(2**N)