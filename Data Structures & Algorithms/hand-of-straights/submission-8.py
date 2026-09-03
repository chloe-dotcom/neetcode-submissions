class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1

        for num in sorted(count):
            needed = count[num]
            if needed == 0:
                continue

            for i in range(needed):
                for curr_num in range(num, num+groupSize):
                    if count.get(curr_num, 0) < 1:
                        return False
                    count[curr_num] -= 1
        return True