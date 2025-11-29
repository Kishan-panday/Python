import numpy as np
arr=np.array([[[1,2,3],
              [4,5,6]], 
              [[5,8,9], 
               [9,0,1]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# import numpy as np

# arr = np.array([1, 2, 3, 1, 5, 1])

# newarr = np.where(arr%2==0)

# print(newarr)