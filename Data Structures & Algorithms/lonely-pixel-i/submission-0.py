class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        r_dict = defaultdict(lambda: None)
        c_dict = defaultdict(lambda: None)

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    if r_dict[i] == True:
                        r_dict[i] = False
                    if c_dict[j] == True:
                        c_dict[j] = False
                    
                    if r_dict[i] == None:
                        r_dict[i] = True
                    if c_dict[j] == None:
                        c_dict[j] = True
        
        count = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and r_dict[i] == True and c_dict[j] == True:
                    count += 1
        return count
                    
                    
        