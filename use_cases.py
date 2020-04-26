'''
This file is used to illustrate uses of methods
Basically a unit test file without the formalities
'''

from bag_of_tricks import BagOfTricks


'''
Lets use kadane

Given arr = [-1,-4,3,2,-6,-1,5,-2,4]

Max sub array should be [5,-2,4] = -7
'''
arr = [-1,-4,3,2,-6,-1,5,-2,4]

obj = BagOfTricks()
print(obj.kadane_max_subarray(arr))