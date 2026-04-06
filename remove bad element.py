# cook your dish here
import sys
from collections import Counter

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        
        # Read the array elements
        a = input_data[ptr : ptr + n]
        ptr += n
        
        # Count frequencies
        counts = Counter(a)
        
        # Get the highest frequency
        max_freq = max(counts.values())
        
        # Min operations = Total - Max Frequency
        results.append(str(n - max_freq))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
