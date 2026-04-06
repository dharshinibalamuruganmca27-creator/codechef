# cook your dish here
def digit_sum(n):
    return sum(int(d) for d in str(n))

def solve():
    N = int(input())
    target_parity = digit_sum(N) % 2
    
    X = N + 1
    while digit_sum(X) % 2 == target_parity:
        X += 1
    print(X)

# For multiple test cases
T = int(input())
for _ in range(T):
    solve()
