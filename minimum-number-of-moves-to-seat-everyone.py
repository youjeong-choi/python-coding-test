class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        seats.sort()
        students.sort()
        moves = 0

        for i in range(len(seats)) :
            moves += abs(seats[i] - students[i])

        return moves


class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        return sum(abs(x-y) for x, y in zip(sorted(seats), sorted(students)))