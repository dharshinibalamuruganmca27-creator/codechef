import sys

def solve():
    # Reading input efficiently
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
        
        # Read the sequence of strings
        s = []
        for i in range(n):
            s.append(int(input_data[ptr]))
            ptr += 1
            
        total_skips = 0
        # Iterate through consecutive pairs
        for i in range(n - 1):
            # Distance - 1 gives the number of strings skipped
            total_skips += abs(s[i+1] - s[i]) - 1
            
        results.append(str(total_skips))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
