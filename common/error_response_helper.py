from models.entity_response import EntityResponse
'''
 Description : This Script contains  request handler for exceptions

 Author: Varsha Shukla
 Version: 1.0
'''

def response_bad_request(e):
    '''
    This method handles a bad request
    :param e: Exception
    :return: Error response with a message
    '''
    error_response = EntityResponse(status="FAILED", error_message=f"Issue in field: {e.__context__}")
    return  error_response.to_json()


def response_internal_server_error(e):

    '''
    This method handles a request if it the solution is not valid for the puzzle
    :param e: Exception
    :return: Error response with a message
    '''
    error_response = EntityResponse(status="FAILED", error_message=f"Unexpected error : {e.__context__} has occured")
    return  error_response.to_json()
