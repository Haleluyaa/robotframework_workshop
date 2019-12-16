import win32com.client
from win32com.client import Dispatch
__version__ = '0.0.1'

class ExcelLib():

    def __init__(self):
        ROBOT_LIBRARY_SCOPE = 'GLOBAL'
        ROBOT_LIBRARY_VERSION = __version__
        self.wb = None
        self.xl = None

    def Add_Workbook(self,ExcelPath):
        """
        Add Excel Workbook

        Example:

        | *Keywords*           |  *Parameters*                                      |
        | Add Workbook           |  C:\\Python_Work\\SampleTest.xlsx |

        """
        self.xl = win32com.client.Dispatch('Excel.Application')
        self.wb = self.xl.Workbooks.Add()
        self.wb.SaveAs(ExcelPath)
        self.xl.Application.Quit()

    def Add_WorkSheet(self, SheetName):
        """
        Add Excel WorkSheet

        Example:

        | *Keywords*           |  *Parameters*                                      |
        | Add WorkSheet          |  SheetTest  |

        """
        ws = self.wb.Worksheets.Add()
        ws.Name = SheetName

    def Open_Excel(self, ExcelPath):
        """
        Opens the Excel file to read from the path provided in the file path parameter.

        Arguments:
                |  File Path (string) | The Excel file name or path will be opened.  |
        Example:

        | *Keywords*           |  *Parameters*                                      |
        | Open Excel           |  C:\\Python_Work\\SampleTest.xlsx  |

        """
        self.xl = win32com.client.Dispatch('Excel.Application')
        self.wb = self.xl.Workbooks.Open(ExcelPath)

    def Get_Sheet_Count(self):
        """
        Returns the number of worksheets in the current workbook.

        Example:

        | *Keywords*              |  *Parameters*                                      |
        | Open Excel              |  C:\\Python_Work\\SampleTest.xlsx  |
        | ${sheetcount}    |  Get Sheets Count                                              |

        """
        return self.wb.Worksheets.Count

    def Get_Sheet_Name(self):
        """
        Returns the names of all the worksheets in the current workbook.

        Example:

        | *Keywords*              |  *Parameters*                                      |
        | Open Excel              |  C:\\Python_Work\\SampleTest.xlsx  |
        | ${sheetname}    |  Get Sheets Names                                                    |

        """
        return self.wb.Activesheet.Name

    def Get_Row_Count(self,SheetName):
        """
        Returns the specific number of rows of the sheet name specified.

        Arguments:
                |  Sheet Name (string)  | The selected sheet that the row count will be returned from. |
        Example:

        | *Keywords*          |  *Parameters*                                      |
        | Open Excel          |  C:\\Python_Work\\SampleTest.xlsx                   |
        | ${RowCount}           |  Get Row Count                                     | TestSheet1 |

        """
        ws = self.wb.Worksheets(SheetName)
        allData = ws.UsedRange
        return allData.Rows.Count

    def Get_Column_Count(self,SheetName):
        """
        Returns the specific number of Column of the sheet name specified.

        Arguments:
                |  Sheet Name (string)  | The selected sheet that the row count will be returned from. |
        Example:

        | *Keywords*          |  *Parameters*                                      |
        | Open Excel          |  C:\\Python_Work\\SampleTest.xlsx  |                |
        | ${ColCount}        |  Get Column Count                                        | TestSheet1 |

        """
        ws = self.wb.Worksheets(SheetName)
        allData = ws.UsedRange
        return allData.Columns.Count

    def Read_Cell_Data(self,SheetName,iRow,iCol):
        """
        Uses the column and row to return the data from that cell.

        Arguments:
                |  Sheet Name (string)                      | The selected sheet that the cell value will be returned from.             |
                |  Row (int)                                | The selected row that will be returned from.                   |
                |  Column (int)                             | The selected column that will be returned from.                |
        Example:

        | *Keywords*                |  *Parameters*                                             |
        | Open Excel                |  C:\\Python_Work\\SampleTest.xlsx  |      |
        | ${data}    |  Read Cell Data                                        |  Sheet1  |   1  |   1  |

        """
        ws = self.wb.Worksheets(SheetName)
        allData = ws.UsedRange
        return allData.Cells(int(iRow),int(iCol))

    def Read_Cell_Data_By_Name(self,SheetName,CellName):
        """
        Uses the cell name to return the data from that cell.

        Arguments:
                |  Sheet Name (string)                      | The selected sheet that the cell value will be returned from.             |
                |  Cell Name (string)                       | The selected cell name that the value will be returned from.              |
        Example:

        | *Keywords*                |  *Parameters*                                             |
        | Open Excel                |  C:\\Python_Work\\SampleTest.xlsx  |      |
        | ${data}    |  Read Cell Data By Name                                      |  Sheet1  |   A1  |     |

        """
        ws = self.wb.Worksheets(SheetName)
        allData = ws.UsedRange
        return allData.Range(CellName)

    def Write_Cell_Data(self,SheetName,iRow,iCol,TestData):
        """
        Write data to cell by using the column and row.

        Arguments:
                |  Sheet Name (string)                      | The selected sheet that the cell will be modified from.                       |
                |  Row (int)                                | The selected row that will be used to modify from.                   |
                |  Column (int)                             | The selected column that will be used to modify from.                |
                |  Value (string)   | Raw value or string value    |
        Example:

        | *Keywords*            |  *Parameters*                                                                     |
        | Open Excel            |  C:\\Python_Work\\SampleTest.xlsx  |                      |       |
        | Write Cell Data |  Sheet1                                        |  1  |    1    |  SampleData     |

        """
        ws = self.wb.Worksheets(SheetName)
        ws.Cells(int(iRow),int(iCol)).Value = TestData

    def Write_Cell_Data_By_Name(self,SheetName,CellName,TestData):
        """
        Write data to cell by using the given sheet name and the given cell that defines by name.

        Arguments:
                |  Sheet Name (string)                      | The selected sheet that the cell will be modified from.                       |
                |  Cell Name (string)                       | The selected cell name that will be used to modified from.                  |
                |  Value (string)   | Raw value or string value    |
        Example:

        | *Keywords*            |  *Parameters*                                                                     |
        | Open Excel            |  C:\\Python_Work\\SampleTest.xlsx  |                      |       |
        | Write Cell Data By Name |  Sheet1                                        |  A2  |  SampleData           |       |

        """
        ws = self.wb.Worksheets(SheetName)
        ws.Range(CellName).Value = TestData

    def Clear_Cell_Data(self,SheetName,iRow,iCol):
        """
        Delete cell data by using the column and row.

        Arguments:
                |  Sheet Name (string)                      | The selected sheet that the cell will be clear value.                       |
                |  Row (int)                                | The selected row that will be used to clear value.                   |
                |  Column (int)                             | The selected column that will be used to clear value.                |
        Example:

        | *Keywords*            |  *Parameters*                                                                     |
        | Open Excel            |  C:\\Python_Work\\SampleTest.xlsx  |                      |       |
        | Clear Cell Data |  Sheet1                                        |  1  |    1    |       |

        """
        ws = self.wb.Worksheets(SheetName)
        ws.Cells(int(iRow),int(iCol)).Value = ''

    def Clear_Cell_Data_By_Name(self,SheetName,CellName):
        """
        Delete cell data by using the given sheet name and the given cell that defines by name.

        Arguments:
                |  Sheet Name (string)                      | The selected sheet that the cell will be clear value.                       |
                |  Cell Name (string)                       | The selected cell that will be used to clear value.                  |
        Example:

        | *Keywords*            |  *Parameters*                                                                     |
        | Open Excel            |  C:\\Python_Work\\SampleTest.xlsx  |                      |       |
        | Clear Cell Data By Name |  Sheet1                                        |  A1  |        |       |

        """
        ws = self.wb.Worksheets(SheetName)
        ws.Range(CellName).Value = ''

    def Save_Excel(self):
        """
        Saves the Excel file that was opened to write before.

        Example:

        | *Keywords*            |  *Parameters*                                      |
        | Open Excel            |  C:\\Python_Work\\SampleTest.xlsx  |                  |
        | Write Cell Data       |  TestSheet1                                        |  Sheet1  |  1    |  1  |  SampleData  |
        | Save Excel            |                                                    |                  |

        """
        self.wb.Save()

    def Save_As_Excel(self,ExcelPath):
        """
        Saves the Excel file that was opened to destination path

        Example:

        | *Keywords*            |  *Parameters*                                      |
        | Open Excel  |  C:\\Python_Work\\SampleTest.xlsx  |                  |
        | Write Cell Data       |  TestSheet1                                        |  Sheet1  |  1    |  1  |  SampleData  |
        | Save As Excel           |  C:\\Python_Work\\SampleTest.xlsx  |                                                |                  |

        """
        self.wb.SaveAs(ExcelPath)



    def Close_Excel(self):
        """
        Close the Excel file

        Example:

        | *Keywords*            |  *Parameters*                                      |
        | Open Excel            |  C:\\Python27\\ExcelRobotTest\\ExcelRobotTest.xlsx  |                  |
        | Write Cell Data       |  TestSheet1                                        |  Sheet1  |  1    |  1  |  SampleData  |
        | Close Excel          |    |                                                |                  |

        """
        self.wb.Close()
        self.xl.Quit()
        self.xl = None

    def Read_Checkbox(self, SheetName, CheckboxName):
        """
        Returns the value of checkbox object in the selected worksheet.

        Arguments:
                |  Sheet Name (string)                      | The selected sheet that the checkbox value will be returned from.             |
                |  CheckboxName (string)                                | The checkbox object.                   |
        Example:

        | *Keywords*                |  *Parameters*                                             |
        | Open Excel                |  C:\\Python_Work\\SampleTest.xlsx  |      |
        | ${data}    |  Read_Checkbox                                        |  Sheet1  |   Check Box 1  |

        """
        ws = self.wb.Worksheets(SheetName)
        for cb in ws.CheckBoxes():
            if CheckboxName == cb.Name:
                if cb.Value == 1:
                    chk_value = True
                else:
                    chk_value = False

                return chk_value

        return None # Any case not found