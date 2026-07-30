class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = -1

        for i in range(len(arr) - 1, -1, -1):
            old_val = arr[i]
            arr[i] = max_element
            if old_val > max_element:
                max_element = old_val
        return arr

            
            
