from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    left = 0
    right = k - 1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    left = k
    right = len(arr) - 1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    left = 0
    right = len(arr) - 1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return deque(arr)



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
