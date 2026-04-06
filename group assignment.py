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
        
        # Count how many people want each specific group size
        preferences = []
        for _ in range(n):
            preferences.append(int(input_data[ptr]))
            ptr += 1
            
        counts = Counter(preferences)
        
        possible = True
        for size, num_people in counts.items():
            if num_people % size != 0:
                possible = False
                break
        
        results.append("YES" if possible else "NO")
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
