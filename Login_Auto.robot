*** Settings ***  
Test Setup    Open Browser To Login Page
Test Template    Login with Valid Credentials Successful
Resource    resource.robot
  

*** Test Case ***             User Name            Password
Valid Username Credentials    ${VALID USERNAME}[0]    ${VALID PASSWORD}[0]
Valid Phone Credentials    ${VALID USERNAME}[1]    ${VALID PASSWORD}[1]

*** Keywords ***
Login with Valid Credentials Successful
    [Arguments]    ${username}    ${password}
    Input Username    ${username}
    Input Password    ${password}
    Log    ${password}
    Submit Credentials
    Verify Login sucessful
     

    