*** Settings ***  
Test Setup    Open Browser To Login Page
Test Template    Login with Valid Credentials Successful
Resource    resource.robot
  

*** Test Case ***    User Name            Password
Valid Credentials    ${VALID USERNAME}    ${VALID PASSWORD}

*** Keywords ***
Login with Valid Credentials Successful
    [Arguments]    ${username}    ${password}

    Input Username    ${username}
    Input Password    ${password}
    Submit Credentials
    Verify Login sucessful
     

    