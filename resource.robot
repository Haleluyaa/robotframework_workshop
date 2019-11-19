*** Settings ***
Library    SeleniumLibrary
Library    ./LineNoti.py

*** Variable ***
${SERVER}    https://www.facebook.com
${BROWSER}    chrome
${DELEY}    0
${VALID USERNAME}    haleluyaa.aki@gmail.com
${VALID PASSWORD}    @Chai4704183;
${line_token}    3twZqE76XkRIldgV4DhO0XohPKRA5OGeTrClGT53ie0
${message}    Hello boy

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${SERVER}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELEY}
    

Input Username
    [Arguments]    ${VALID USERNAME}
    Input Text    //input[@id='email']    ${VALID USERNAME}

Input Password
    [Arguments]    ${VALID PASSWORD}
    Input Text    //input[@id='pass']    ${VALID USERNAME}

Submit Credentials
    Click Button    //input[contains(@type, 'submit')]

Line Notification
    [Arguments]    ${line_token}    ${message}
    Set Line Token    ${line_token}
    Line Text    ${message}  
    Line Sticker    2    507