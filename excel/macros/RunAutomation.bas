Attribute VB_Name = "RunAutomation"
Option Explicit

Public Sub RunAutomation()
    Dim projectRoot As String
    Dim command As String
    Dim exitCode As Long

    projectRoot = ThisWorkbook.Path & Application.PathSeparator & ".." & Application.PathSeparator & ".."
    command = "cmd /c cd /d """ & projectRoot & """ && python -m excel_automation_toolkit run " & _
              "--input data/raw/sample_sales.csv " & _
              "--output data/processed/automation_report.xlsx " & _
              "--date-column ""Order Date"" " & _
              "--numeric-column Revenue " & _
              "--numeric-column Units " & _
              "--dimension Region " & _
              "--amount-column Revenue"

    exitCode = Shell(command, vbNormalFocus)
    If exitCode = 0 Then
        MsgBox "Unable to start the Python automation process.", vbCritical
    Else
        MsgBox "Automation started. Check data/processed/automation_report.xlsx when it completes.", vbInformation
    End If
End Sub

