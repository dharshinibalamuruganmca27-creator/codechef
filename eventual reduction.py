t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    possible = True
    
    for v in freq.values():
        if v % 2 != 0:
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")
