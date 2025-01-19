def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
numbers = [10, 23, 45, 70, 11, 15]
target = 70

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
