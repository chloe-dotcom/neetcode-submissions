class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combinedCars = [(u, v) for u, v in zip(position, speed)]
        combinedCars = sorted(combinedCars, key=lambda x: x[0], reverse=True)
        fleets = 1
        prevTime = (target-combinedCars[0][0]) / combinedCars[0][1]
        for i in range(1, len(combinedCars)):
            currCar = combinedCars[i]
            currTime = (target-currCar[0])/currCar[1]
            if currTime > prevTime:
                fleets+=1
                prevTime = currTime
        return fleets