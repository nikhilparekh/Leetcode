class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        c = 0
        for i in range(len(seats)):
            c+=abs(seats[i]-students[i])
        return c