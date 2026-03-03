import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    pointer = 1
    
    results = []
    for _ in range(T):
        N = int(input_data[pointer])
        pointer += 1
        
        # We only care about the sum of elements in B
        b_sum = 0
        for i in range(N):
            b_sum += int(input_data[pointer])
            pointer += 1
            
        # Check if the sum of B is even
        if b_sum % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
