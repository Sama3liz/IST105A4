import sys
import math

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    
    if a < 1:
        print("<h3>Value for a must be above 1</h3>")
    elif c < 0:
        print("<h3>Value for c cannot be negative... you are going to get your windows freeze</h3>")
    else:
        if b == 0:
            print("<h3>b is zero but that does not affect nothhing</h3>")
        
        c_cubed = c ** 3
        print(f"<h3>C Cubed: {c_cubed}</h3>")
        root = math.sqrt(c_cubed)
        
        if c_cubed > 1000:
            print("<h3>Multiplying the square root of cube by 10</h3>")
            root *= 10
        else:
            print("<h3>Dividing the square root of cube by a</h3>")
            root /= a
        
        print("<h3>Adding b to result</h3>")
        root += b
        
        print(f"<h3>Computed Result (Two decimals): {root:.2f}</h3>")
except ValueError:
    print("<h3>Error: All inputs must be numeric.</h3>")
