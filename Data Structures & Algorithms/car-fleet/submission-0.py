class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_and_speed = sorted(zip(position, speed), reverse=True)
        for pos, speed in pos_and_speed:
            time_to_destination = (target-pos)/speed
            stack.append(time_to_destination) 
            if len(stack)>1 and stack[-1]<=stack[-2]: 
                stack.pop(-1)
        return len(stack)