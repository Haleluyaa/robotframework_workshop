*** Settings ***  
Test Setup    Open Browser To Login Page
Test Template    Login with Valid Credentials Successful
Resource    resource.robot
  

*** Test Case ***             User Name            Password                     verify
Valid Username Credentials    ${VALID USERNAME}[0]    ${VALID PASSWORD}[0]    ${Verify_Login}[0]
Valid Phone Credentials    ${VALID USERNAME}[1]    ${VALID PASSWORD}[1]    ${Verify_Login}[1]    
Valid Natty Credentials    ${VALID USERNAME}[2]    ${VALID PASSWORD}[2]    ${Verify_Login}[2] 
*** Keywords ***
Login with Valid Credentials Successful
    [Arguments]    ${username}    ${password}    ${verify}
    Input Username    ${username}
    Input Password    ${password}
    Log    ${password}
    Submit Credentials    
    Verify Login sucessful    ${verify}
    Close Browser
     

    