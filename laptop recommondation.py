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
        ptr += 1
        
        # Recommendations for laptops 1 to 10
        recommendations = list(map(int, input_data[ptr : ptr + n]))
        ptr += n
        
        counts = Counter(recommendations)
        
        # Find the maximum frequency
        max_freq = max(counts.values())
        
        # Find which laptops have this maximum frequency
        best_laptops = [laptop for laptop, freq in counts.items() if freq == max_freq]
        
        if len(best_laptops) > 1:
            results.append("CONFUSED")
        else:
            results.append(str(best_laptops[0]))
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
