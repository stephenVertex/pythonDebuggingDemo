from typing import List

print("Welcome to scriptAlpha")

variableX = 10

for i in range(10):
    varyableX = variableX + i * 10

print(f"{variableX=}")


def addNumbers(xl: List[int]):
    return(sum(xl))

nums = [1,2,3,4,5]
lets = ['a', 'b', 'c']
print(f"Adding some numbers {addNumbers(nums)}")

print(f"Adding some letters {addNumbers(lets)}") ## mypy will catch this
