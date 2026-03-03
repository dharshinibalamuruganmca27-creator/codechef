import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    ptr = 1
    
    results = []
    for _ in range(T):
        N = int(input_data[ptr])
        K = int(input_data[ptr + 1])
        ptr += 2
        
        A = list(map(int, input_data[ptr : ptr + N]))
        ptr += N
        
        current_storage = 0
        failed_day = -1
        
        for i in range(N):
            current_storage += A[i]
            if current_storage >= K:
                current_storage -= K
            else:
                # Days are 1-indexed in the problem
                failed_day = i + 1
                break
        
        if failed_day == -1:
            results.append("YES")
        else:
            results.append(f"NO {failed_day}")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
