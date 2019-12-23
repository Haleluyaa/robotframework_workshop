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
#${row_count}    5

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${SERVER}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELEY}
    #Page Should contain Element    //input[@id='email']
    Import Test Data
    Log List    ${VALID USERNAME}
    Log List    ${VALID PASSWORD}
    
    

Input Username
    [Arguments]    ${VALID_user}
    Input Text    //input[@name='email']    ${VALID_user}

Input Password
    [Arguments]    ${VALID_pw}
    Input Text    //input[@id='pass']    ${VALID_pw}

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
    ${row_count}=    Convert To Integer    ${row_count}
    ${row_count}=    Evaluate    ${row_count} + 1
    Log to console    ${row_count}
    :FOR    ${i}    IN RANGE    3    ${row_count}
    \    ${usr_temp} =    Read Cell Data    Login_valid    ${i}    2
    \    ${usr_temp} =    Convert To String    ${usr_temp}           
    \    Append To List    ${VALID USERNAME}    ${usr_temp}                    
    \    ${ps_temp} =    Read Cell Data    Login_valid    ${i}    3 
    \    ${ps_temp} =    Convert To String    ${ps_temp}  
    \    Append To List    ${VALID PASSWORD}    ${ps_temp} 
    Log to console    ${VALID USERNAME}    
    Log to console    ${VALID PASSWORD}
    Close Excel
    #${VALID_user} =    Convert To String    ${VALID USERNAME}
    #${VALID_pw} =    Convert To String    ${VALID PASSWORD} 
    #Return    @{VALID USERNAME}     


    
