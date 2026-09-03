class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        open_groups = 0
        last_num = -1
        q = deque()
        for num in sorted(count):
            if ((open_groups > 0 and num > last_num + 1) or open_groups > count[num]):
                return False
            new_group= count[num] - open_groups
            q.append(new_group)
            last_num = num
            open_groups += new_group
            if len(q) == groupSize:
                open_groups -= q.popleft()
    
        return open_groups == 0
