import numpy as np
import time
arr = np.arange(1,1000001)

# start = time.time()
# sqr = [x**2 for x in arr]
# end = time.time()

# print(end-start)

start = time.time()
sqr = arr**2
end = time.time()

print(end-start)