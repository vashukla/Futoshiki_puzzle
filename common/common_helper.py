from typing import List

'''
 Description : This Script contains  common/resuable utility methods

 Author: Varsha Shukla
 Version: 1.0
'''

def validate_dim(grid:List[List]) -> bool:
    '''
    This methos is used to check if the solution entered by user has expected format
    :param grid: Puzzle solution passed by the user
    :return:
         Boolean: True/False
    '''

    valid = True
    number_of_rows = len(grid)
    for line in grid:
        if len(line) != number_of_rows:
            valid = False
            break

    return valid