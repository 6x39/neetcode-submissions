class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # look for the target number in the list, if it exists, look for a value of 0.
        # no 0, look for a value x less than the target (iterate) and then search for a value x in the list.
        # if that doesn't exist, it checks for negative values instead. we can integrate this with the earlier ones.

        if target in numbers and 0 in numbers and target != 0:
            return self.larger(target, 0, numbers)

        p1 = 0
        p2 = len(numbers) - 1
        while True:
            if numbers[p1] + numbers[p2] == target:
                return self.larger(numbers[p1], numbers[p2], numbers)
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
    
    def larger(self, point1, point2, numbers): # search after the first index to find the second one.
        if point1 < point2:
            return [numbers.index(point1) + 1, numbers.index(point2) + 1]
        else:
            if point1 == point2:
                return [numbers.index(point1) + 1, numbers.index(point2, numbers.index(point1) + 1) + 1]
            return [numbers.index(point2)+ 1, numbers.index(point1) + 1]

    


            



        

        

        