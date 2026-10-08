class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(u, v) for u, v in zip(position, speed)]
        combined.sort(reverse = True, key=lambda x:x[0])

        prevTime = (target - combined[0][0]) / combined[0][1]

        fleets = len(combined)
        for car in range(1, len(combined)):
            currentCar = combined[car]
            currentTime = (target - currentCar[0])/currentCar[1]
            if currentTime <= prevTime:
                fleets -= 1
            else:
                prevTime = currentTime
        return fleets