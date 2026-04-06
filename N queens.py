import sys

def solve():
    # Read input from standard input
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
        
        # Calculate (0.143 * N)^N
        value = (0.143 * n) ** n
        
        # Round to the nearest integer
        # We use int(value + 0.5) to ensure 0.5 rounds up correctly
        rounded_value = int(value + 0.5)
        
        results.append(str(rounded_value))
        
    # Print all results separated by newlines
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
