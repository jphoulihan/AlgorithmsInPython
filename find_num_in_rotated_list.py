from binary_search import *


# returns the index of a number in a rotated list

def find_num_in_rotated_list(nums, query, search_range):
    if query > nums[0]:
        start = 0
        end = search_range
    else:
        start = search_range
        end = len(nums) - 1

    def condition(mid):

        if nums[mid] == query:
            return 'found'
        elif nums[mid] > query:
            return 'left'
        else:
            return 'right'

    return binary_search(start, end, condition)