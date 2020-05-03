from flask import Flask, request
from werkzeug.exceptions import InternalServerError
from modules.validate.validate_puzzle_service import get_puzzle_validate_request, validate_puzzle
from common.error_response_helper import response_bad_request, response_internal_server_error

'''
 Description : This Script creates a Post API 

 Author: Varsha Shukla
 Version: 1.0
'''

app = Flask(__name__)


@app.errorhandler(InternalServerError)
def handle_bad_request(e):
    '''
    This method handles a bad request
    :param e: exception
    :return: response message
    '''
    return response_bad_request(e), 500


@app.route('/validate', methods=['POST'])
def validate_futoshiki_puzzle():
    '''
    This method responds success and failure of the request made
    '''
    args = request.get_data()
    try :
        puzzle = get_puzzle_validate_request(args=args)
        result = validate_puzzle(puzzle)
        return f"result:{str(result)}",200
    except Exception as e:
        print(f"Error Occured : {e}")


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
