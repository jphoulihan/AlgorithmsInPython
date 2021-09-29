from binary_search import *


# find how many times a sorted list has been rotated
def rotated_list_counter(nums):
    def condition(mid):
        if nums[mid] < nums[mid - 1]:
            return 'found'
        elif nums[mid] < nums[len(nums) - 1]:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums) - 1, condition)