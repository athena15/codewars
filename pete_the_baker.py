# https://www.codewars.com/kata/pete-the-baker

class Solution:
    def cakes(self, recipe, available):
        possible_cakes = []
        for ingredient, quantity in recipe.items():
            possible_cakes.append(available.get(ingredient, 0) // quantity)

        return min(possible_cakes)


# alternatively, use a concise list comprehension with:
class Solution_2:
    def cakes(self, recipe, available):
        return min([available.get(ingredient, 0) // quantity for ingredient, quantity in recipe.items()])


if __name__ == '__main__':
    solution = Solution()
    solution.cakes(recipe={"flour": 500, "sugar": 200, "eggs": 1},
                   available={"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})  # returns 2
