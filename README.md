# APP.VWO.LOGIN

## **Tech Stack

1. Python 3.12
2. Requests -HTTP Requests
3. Pytest -Testing Framework
4. Reporting - Allure Report, Pytest HTML Report
5. Test Data - CSV,EXCEL, JSON

## *** Framework for API Testing python packages

src
    -helpers
        -api_requests_wrapper.py
        -common_verification.py
        -payload_manager.py
        -utils.py
    -constants
        -api_constants,py
    -resource

tests
    -integration_tests

## ***Install Packages

1. pip list
2. pip freeze >requirement.text
3. pip install -r requirement.text  
4. pip install pytest 
5. pip install requests 
6. pip install pytest-html 
6. pip install faker 
7. pip install openpyxl 
8. pip install xdist
8. pip install jsonschema
9. pip install fixture


# To Install Allure Reports Command:-

9. pip install allure-pytest
10. node --version
10. npm --version  
11. npm i -g allure-commandline
12. allure serve reports

## To execute the HTML report command

pytest FileName.py --html=report.html

## To execute the allure report command

pytest FileName.py --alluredir=reports
allure serve reports

## Command to execute 

 pytest FileName.py -s -v 


## github first time Commands
1. git init
2. git add . 
3. git commit -m "first commit"
4. git branch -M main
5. git remote add origin "Created New git path" 
6. git push -u origin main

## Afterward git push commands

1. git add "Name of folder" or git add .
2. git commit -m "Message"
3. git pull
4. git push








