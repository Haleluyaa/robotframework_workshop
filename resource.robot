*** Settings ***
Library    SeleniumLibrary
Library    ./LineNoti.py

*** Variable ***
${SERVER}    https://www.facebook.com
${BROWSER}    chrome
${DELEY}    0
${VALID USERNAME}    haleluyaa.aki@gmail.com
${VALID PASSWORD}    xxxxxxx
${line_token}    3twZqE76XkRIldgV4DhO0XohPKRA5OGeTrClGT53ie0
<<<<<<< HEAD
${message}    Fail happen!!! 

=======
${message}    Hello boy
>>>>>>> 1fca072e883e2b8808e53544ee1819cbc7918245

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
    Input Text    //input[@id='pass']    ${VALID PASSWORD}

Submit Credentials
    Click Button    //input[contains(@type, 'submit')]

Verify Login sucessful
    ${CheckRs} =    Run Keyword And Return Status    Page Should Contain Element    //div[text()='ธนาวิทย์ ชัยสุภาพสิริกุล']
    Run Keyword If    not ${CheckRs}    Line Notification    ${line_token}    ${message}

    #Ref. https://stackoverflow.com/questions/44758541/compare-false-expression-in-robot-framework-test-cases
    #Log To Console    ${CheckRs}
    #Run Keyword And Ignore Error| Keyword | locator...
    #Line Notification ${line_token}    ${message}

Line Notification
    [Arguments]    ${line_token}    ${message}
    Set Line Token    ${line_token}
<<<<<<< HEAD
    Line Text    ${message}
    Line sticker    2    154
    Line pic    D://Initial Training//Software coding//Software Testing//Robot//robotframework_workshop//selenium-screenshot-26.png      
=======
    Line Text    ${message}  
    Line Sticker    2    507
>>>>>>> 1fca072e883e2b8808e53544ee1819cbc7918245
