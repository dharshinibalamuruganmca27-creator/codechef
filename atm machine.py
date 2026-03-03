import sys

def solve():
    # Use fast I/O for competitive programming
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    T = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(T):
        # N = number of people, K = total money
        N = int(input_data[idx])
        K = int(input_data[idx+1])
        idx += 2
        
        # A = list of withdrawal amounts
        A = input_data[idx : idx + N]
        idx += N
        
        current_res = ""
        for amount_str in A:
            amount = int(amount_str)
            if amount <= K:
                # Successful withdrawal
                current_res += "1"
                K -= amount
            else:
                # Insufficient funds
                current_res += "0"
        
        results.append(current_res)
    
    # Print each binary string on a new line
    print("\n".join(results))

if __name__ == "__main__":
    solve()
