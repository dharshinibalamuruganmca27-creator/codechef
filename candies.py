import sys
from collections import Counter

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    pointer = 1
    
    results = []
    for _ in range(T):
        N = int(input_data[pointer])
        pointer += 1
        
        # There are 2*N prices to read
        prices = input_data[pointer : pointer + (2 * N)]
        pointer += 2 * N
        
        # Count the frequency of each price
        counts = Counter(prices)
        
        is_possible = True
        for p in counts:
            if counts[p] > 2:
                is_possible = False
                break
        
        results.append("Yes" if is_possible else "No")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
