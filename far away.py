import sys

def solve():
    # Read all input at once for speed
    input = sys.stdin.read().split()
    if not input:
        return
        
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr+1])
        ptr += 2
        
        max_dist = 0
        for _ in range(n):
            a_i = int(input[ptr])
            # The furthest point is always 1 or M
            max_dist += max(abs(a_i - 1), abs(a_i - m))
            ptr += 1
            
        results.append(str(max_dist))
    
    # Print all results at once
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()
