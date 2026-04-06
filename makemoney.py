# cook your dish here
import sys

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
        x = int(input_data[ptr+1])
        c = int(input_data[ptr+2])
        ptr += 3
        
        total_coins = 0
        total_cost = 0
        
        for _ in range(n):
            a_i = int(input_data[ptr])
            ptr += 1
            
            # Check if upgrading the bag is profitable
            if (x - a_i) > c:
                total_coins += x
                total_cost += c
            else:
                total_coins += a_i
        
        results.append(str(total_coins - total_cost))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
