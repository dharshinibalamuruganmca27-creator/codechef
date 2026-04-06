import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        s = input_data[ptr+1]
        ptr += 2
        
        # Check if any character appears more than once
        counts = Counter(s)
        has_duplicate = False
        for char in counts:
            if counts[char] >= 2:
                has_duplicate = True
                break
        
        if has_duplicate:
            # Keep only two identical characters, delete the rest
            results.append(str(n - 2))
        else:
            results.append("-1")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
