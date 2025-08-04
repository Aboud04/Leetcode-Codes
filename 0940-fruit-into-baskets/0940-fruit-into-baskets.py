class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = dict()
        l = 0
        max_count = 0

        for r in range(len(fruits)):
            fruit = fruits[r]
            d[fruit] = d.get(fruit, 0) + 1

            while len(d) > 2:
                left_fruit = fruits[l]
                d[left_fruit] -= 1
                if d[left_fruit] == 0:
                    del d[left_fruit]
                l += 1

            max_count = max(max_count, r - l + 1)

        return max_count
