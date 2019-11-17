*** Settings ***
Library    SeleniumLibrary

*** Variable ***
${SERVER}    https://www.facebook.com
${BROWSER}    chrome
${DELEY}    0
${VALID USERNAME}    haleluyaa.aki@gmail.com
${VALID PASSWORD}    @Chai4704183;

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