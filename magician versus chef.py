import sys

def solve():
    # Read N (boxes), X (initial pos), S (swaps)
    line1 = sys.stdin.readline().split()
    if not line1: return
    n, current_pos, s = map(int, line1)
    
    for _ in range(s):
        a, b = map(int, sys.stdin.readline().split())
        # If the coin is in one of the swapped boxes, update its position
        if current_pos == a:
            current_pos = b
        elif current_pos == b:
            current_pos = a
            
    print(current_pos)

t_str = sys.stdin.readline().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        solve()
