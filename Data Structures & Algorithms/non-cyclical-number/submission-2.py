class Solution:
    def isHappy(self, n: int) -> bool:
        has_been_seen = []
        count = 0
        while not (n in has_been_seen):
            if count > 0:
                has_been_seen.append(sum_of_squares)
            sum_of_squares = 0
            n_string = str(n)
            for i in range(0, len(n_string)):
                sum_of_squares += int(n_string[i]) ** 2
            n = sum_of_squares
            print(n)
            if n == 1:
                return True
            count += 1
        return False