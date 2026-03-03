import sys

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    pointer = 1
    
    results = []
    for _ in range(T):
        # Dragon's scores
        d_dsa = int(input_data[pointer])
        d_toc = int(input_data[pointer + 1])
        d_dm = int(input_data[pointer + 2])
        pointer += 3
        
        # Sloth's scores
        s_dsa = int(input_data[pointer])
        s_toc = int(input_data[pointer + 1])
        s_dm = int(input_data[pointer + 2])
        pointer += 3
        
        # Calculate totals
        d_total = d_dsa + d_toc + d_dm
        s_total = s_dsa + s_toc + s_dm
        
        # Comparison Logic
        if d_total > s_total:
            results.append("DRAGON")
        elif s_total > d_total:
            results.append("SLOTH")
        else:
            # Tie-break 1: DSA
            if d_dsa > s_dsa:
                results.append("DRAGON")
            elif s_dsa > d_dsa:
                results.append("SLOTH")
            else:
                # Tie-break 2: TOC
                if d_toc > s_toc:
                    results.append("DRAGON")
                elif s_toc > d_toc:
                    results.append("SLOTH")
                else:
                    # Everything is tied
                    results.append("TIE")
                    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
