*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    ./LineNoti.py
Library    ./ExcelLib.py

*** Variable ***
${SERVER}    https://www.facebook.com
${BROWSER}    chrome
${DELEY}    0
@{VALID USERNAME}    
@{VALID PASSWORD}    
${line_token}    3twZqE76XkRIldgV4DhO0XohPKRA5OGeTrClGT53ie0
${message}    Fail happen!!!
${excel_path}    D:\\template_Works\\robotframework_workshop\\Facebook_testingxlsx.xlsx


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${SERVER}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELEY}
    #Page Should contain Element    //input[@id='email']
    Import Test Data
    

Input Username
    [Arguments]    ${VALID USERNAME}
    Input Text    //input[@name='email']    ${VALID USERNAME}

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
    Line Text    ${message}
    Line sticker    2    154
    Line pic    D:/template_Works/robotframework_workshop

Import Test Data
    Open Excel    ${excel_path}
    ${row_count}    Get Row Count    Login_valid
    Log to console    ${row_count}
    :FOR    ${i}    IN RANGE    3    ${row_count}
    \    ${usr_temp} =    Read Cell Data    Login_valid    ${i}    2       
    \    Log to console    ${usr_temp} 
    \    Append To List    ${VALID USERNAME}    ${usr_temp}                    
    \    Log to console    ${VALID USERNAME}
    \    ${ps_temp} =    Read Cell Data    Login_valid    ${i}    3    
    \    Log to console    ${ps_temp}
    \    Append To List    ${VALID PASSWORD}    ${ps_temp}     
    \    Log to console    ${VALID PASSWORD}    


    
