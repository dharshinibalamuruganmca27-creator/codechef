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
        ptr += 1
        
        # Read goals (A) and fouls (B) for all N players
        goals = [int(x) for x in input_data[ptr : ptr + n]]
        ptr += n
        fouls = [int(x) for x in input_data[ptr : ptr + n]]
        ptr += n
        
        max_points = 0
        for i in range(n):
            # Calculate points: 20 per goal, -10 per foul
            current_score = (goals[i] * 20) - (fouls[i] * 10)
            
            # Score cannot be negative
            if current_score < 0:
                current_score = 0
            
            # Track the maximum score found
            if current_score > max_points:
                max_points = current_score
                
        results.append(str(max_points))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
