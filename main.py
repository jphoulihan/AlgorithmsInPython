from card_finder import *
from find_num_in_rotated_list import *
from rotated_list_counter import *

nums = [5, 6, 9, 0, 2, 3, 4]
cards = [0, 1, 1, 2, 3, 4, 5, 6, 7, 88]

search_range = rotated_list_counter(nums)
list_length = len(nums)-1

query_1 = 2
pos = find_num_in_rotated_list(nums, query_1, search_range)

print('Value', query_1, 'was found at index', pos, 'of the rotated list')

query_2 = 88
print('Value', query_2, 'was found at index', card_finder(cards, query_2), 'of the ascending list')
