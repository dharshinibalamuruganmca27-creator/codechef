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
        ptr += 1
        
        fingers = list(map(int, input_data[ptr : ptr + n]))
        ptr += n
        sheaths = list(map(int, input_data[ptr : ptr + n]))
        ptr += n
        
        front = True
        back = True
        
        for i in range(n):
            # Check front orientation
            if fingers[i] > sheaths[i]:
                front = False
            # Check back orientation (flipped sheaths)
            if fingers[i] > sheaths[n - 1 - i]:
                back = False
                
        if front and back:
            results.append("both")
        elif front:
            results.append("front")
        elif back:
            results.append("back")
        else:
            results.append("none")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
