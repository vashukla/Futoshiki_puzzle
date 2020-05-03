from dataclasses import  dataclass
from dataclasses_json import dataclass_json
from typing import Optional
'''
 Description : This Script contains  class for the API response

 Author: Varsha Shukla
 Version: 1.0
'''



@dataclass_json
@dataclass
class EntityResponse:
    status: str
    error_message: Optional[str] = None