'''
 Description : The purpose of this script is to check the functionality of methods using unit test cases

 Author: Varsha Shukla
 Version: 1.0
'''


import unittest
from common.common_helper import validate_dim



class Testing(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """

    def setUp(self):

        self.grid = [[6,3,2,4,5,1],[1,6,3,5,2,4],[3,5,1,6,4,2],[2,4,6,3,1,5],[5,2,4,1,3,6],[4,1,5,2,1,1,1,1,11,1]]
        print(type(self.grid))

    def test_validate_dim(self):
        '''
        This method tests if the user input has a valid format
        :return: False
        '''
        test_grid = validate_dim(self.grid)
        self.assertFalse(test_grid)




if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()