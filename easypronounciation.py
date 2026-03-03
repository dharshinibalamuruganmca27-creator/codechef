# cook your dish here
import sys

def solve():
    # Read number of test cases
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    vowels = {'a', 'e', 'i', 'o', 'u'}
    idx = 1
    
    results = []
    for _ in range(T):
        N = int(input_data[idx])
        S = input_data[idx + 1]
        idx += 2
        
        consonant_count = 0
        is_hard = False
        
        for char in S:
            if char in vowels:
                consonant_count = 0  # Reset streak if we hit a vowel
            else:
                consonant_count += 1 # Increment streak for consonants
            
            if consonant_count >= 4:
                is_hard = True
                break
        
        results.append("NO" if is_hard else "YES")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
