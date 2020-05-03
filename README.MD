# Futoshiki puzzle solution validator.

This is a project to validate the solution of Futoshiki puzzle.

## Purpose

The purpose of the project is to create a function to validate the solution of Futoshiki Puzzle provided by the user. 


## Output 

Solution is right or not.
It returns Boolean value as TRUE or False
    
## Getting Started

Below instructions can be used to setup and generate the github repo Futoshiki Puzzle
    
### Prerequisite
    
    1. python 3.7 and pip are installed on your machine
    2. Clone the repository , for example ~/code/Futoshiki_puzzle
    3. Postman/curl to hit the API
        
        

    
### Usage

In order to run the project on your own machine, please follow below steps.

    1. Open command prompt and follow below instructions:
                1.1 cd {root_dir}/Futoshiki_puzzle
                1.2 pip install -r requirements.txt  
                1.3 cd {root_dir}/Futoshiki_puzzle/app.py
    2. End point : http://localhost:3000/validate
    3. Json Body(application/json):
        {
        "puzzle": [[6,3,2,4,5,1],[1,6,3,5,2,4],[3,5,1,6,4,2],[2,4,6,3,1,5],[5,2,4,1,3,6],[4,1,5,2,6,3]]
        }
               
    
    
### Thought process behind the design

According to the requirement, I was suppose to create a backend for User Interface.
Hence I have created a API which could be integrated easily with any UI applications.



## Author

* **Varsha Shukla**
