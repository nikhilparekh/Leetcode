class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        for i in asteroids:
            if i>mass:
                return False
            else:
                mass+=i
        return True