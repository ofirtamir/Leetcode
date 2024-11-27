class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[[p,s] for p,s in zip(position, speed)]
        cars.sort()
        stack = []
        for x in range(len(cars)-1,-1,-1):
            if not stack or (target - stack[-1][0])/ (stack[-1][1]) < ((target-cars[x][0])/ cars[x][1]):
                stack.append(cars[x])
            
        return len(stack)