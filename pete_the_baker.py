# https://www.codewars.com/kata/pete-the-baker

class Solution:
    def cakes(self, recipe, available):
        possible_cakes = []
        for ingredient, quantity in recipe.items():
            try:
                possible_cakes.append(available[ingredient] // quantity)
            except KeyError:
                return 0

        return min(possible_cakes)


if __name__ == '__main__':
    solution = Solution()
    solution.cakes(recipe={"flour": 500, "sugar": 200, "eggs": 1},
                   available={"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})  # returns 2
