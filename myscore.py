import sys

def solve():
    # Use fast I/O
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
        
        # Array to store max scores for problems 1 to 8
        # Using index 0-8 (we'll ignore index 0 and 9-11)
        best_scores = [0] * 9
        
        for _ in range(n):
            p = int(input_data[ptr])
            s = int(input_data[ptr+1])
            ptr += 2
            
            # Only update if the problem is scorable (1-8)
            if 1 <= p <= 8:
                if s > best_scores[p]:
                    best_scores[p] = s
        
        # The total score is the sum of max scores of problems 1 to 8
        results.append(str(sum(best_scores)))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
