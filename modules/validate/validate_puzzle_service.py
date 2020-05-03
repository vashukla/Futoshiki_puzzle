from models.puzzle import puzzle_validate_request
from common.common_helper import validate_dim

'''
 Description : The purpose of this script is to check if the given solution of the puzzle
                is valid or not.

 Author: Varsha Shukla
 Version: 1.0
'''


def validate_puzzle(puzzle) -> bool:
    '''

    :param
         puzzle: Puzzle solution passed by the user
    :return:
         Boolean: True/False
    '''

    valid = True
    size = len(puzzle.puzzle)

    if not validate_dim(grid=puzzle.puzzle):
        return False

    for x in range(size):
        visited = set()
        for y in range(size):
            value = puzzle.puzzle[x][y]
            if 1 <= value <= size:
                if value in visited:
                    valid &= False
                else:
                    visited.add(value)
            else:
                valid &= False


    for y in range(size):
        visited = set()
        for x in range(size):
            value = puzzle.puzzle[x][y]
            if 1 <= value <= size:
                if value in visited:
                    valid &= False
                else:
                    visited.add(value)
            else:
                valid &= False

    return valid


def get_puzzle_validate_request(args) ->puzzle_validate_request:

    '''
    This method is used to parse the argument passed by the user
        as Json
    :param
        User Input

    :return:
        List: Puzzle solution
    '''
    return puzzle_validate_request.from_json(args)
