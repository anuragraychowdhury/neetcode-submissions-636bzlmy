# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        left = 0
        right = n - 1

        while left < right:
            if n % 2 == 0:
                first_middle = (left + right) // 2
                second_middle = first_middle + 1
                guess = reader.compareSub(left, first_middle, second_middle, right)
                
                if guess == 1:
                    right = first_middle
                elif guess == -1:
                    left = second_middle
            else:
                middle = (left + right) // 2
                guess = reader.compareSub(left, middle - 1, middle + 1, right)
                
                if guess == 1:
                    right = middle - 1
                elif guess == -1:
                    left = middle + 1
                else:
                    return middle
            n = right - left + 1
        return left
        
        













