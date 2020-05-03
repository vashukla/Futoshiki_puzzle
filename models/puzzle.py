from typing import List
from dataclasses_json import dataclass_json
from dataclasses import  dataclass

'''
 Description : This Script contains a class for the type of request

 Author: Varsha Shukla
 Version: 1.0
'''


@dataclass_json
@dataclass
class puzzle_validate_request:
    puzzle: List[List]
