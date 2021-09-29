from binary_search import *


# find position of a number in an ascending sorted list

def card_finder(cards, query):

    def condition(mid):
        if query == cards[mid]:
            return 'found'
        elif query < cards[mid]:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(cards)-1, condition)