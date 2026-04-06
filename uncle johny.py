import sys

def solve():
    # Reading input efficiently
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
        
        # Read the lengths of the songs
        lengths = []
        for _ in range(n):
            lengths.append(int(input_data[ptr]))
            ptr += 1
            
        # K is the original 1-based position
        k = int(input_data[ptr])
        ptr += 1
        
        # Step 1: Store the length of "Uncle Johny"
        target_length = lengths[k-1]
        
        # Step 2: Sort the playlist
        lengths.sort()
        
        # Step 3: Find the 1-based index in the sorted list
        # Using index() is fine here as N is small (up to 100)
        new_position = lengths.index(target_length) + 1
        results.append(str(new_position))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
