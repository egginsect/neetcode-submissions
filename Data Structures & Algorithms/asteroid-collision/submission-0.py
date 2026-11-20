class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        out = []
        for asteroid in asteroids:
            if asteroid < 0:
                while out and out[-1] > 0 and abs(out[-1])<abs(asteroid):
                    out.pop(-1)
                if out and out[-1]>0:
                    if abs(out[-1]) == abs(asteroid):
                        out.pop(-1)
                        continue
                    else:
                        continue
            out.append(asteroid)
        return out

            