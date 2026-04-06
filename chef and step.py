import sys

def solve():
    # Use fast I/O to read the entire input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        k = int(input_data[ptr+1])
        ptr += 2
        
        case_result = []
        for _ in range(n):
            d_i = int(input_data[ptr])
            ptr += 1
            
            # Check if distance is divisible by step length K
            if d_i % k == 0:
                case_result.append('1')
            else:
                case_result.append('0')
        
        # Combine the individual '0'/'1' into a single string
        results.append("".join(case_result))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
