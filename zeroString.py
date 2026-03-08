t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    ones = s.count('1')
    zeros = n - ones
    
    print(min(ones, 1 + zeros))
