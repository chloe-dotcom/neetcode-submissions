class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        have = [0] * 3
        for trip in triplets:
            skip_check = False
            side_check = [0] * 3
            for i in range(3):
                if trip[i] > target[i]:
                    skip_check = True
                    break
                if trip[i] == target[i]:
                    side_check[i] = 1
            
            if skip_check == False:
                for i in range(3):
                    if side_check[i] == 1:
                        have[i] = 1
            
                if have == [1, 1, 1]:
                    return True
        
        return False
            