Dp Work Automated Testing:

Automated Testing will help team test if all the functionality of the portal is working as per our expectation when any code changes or new functionalities are being added in the DP Work portal.

Pre requisites1 :
------------------
1. Anaconda or miniconda should be installed in executors local system
2. Git if installed will be very much beneficial for collaboration

Environment installation:
----------------------------
In order to install environment in executor's local system:
1. Clone the git repository in local sytem (using the command git clone <repository url> in git bash or dowload the git code in the form of zip folder, extract all and open in Vs code)
2. Open Anaconda promt
3. Check the version of conda installed by using the command (conda --version)
4. Now change the diretory to the project folder using the command (cd <path of the project folder in local system>)
5. Post this run the command to create the virtual environment to run the testCases:
    conda env create -f venv.yml -p ./venv
6. Activate the virtual environment using the command:
    conda activate ./venv

User Inputs that are required for Automated Testing:
-------------------------------------------------------
1. config.ini file should be filled before running any test cases
2. files inside testData folder needs to be filled in before running any test cases
   For now DpWorkDataParameterization.xlsx needs to be filled

Run the testCases:
--------------------------------
Ways
    1. Using the repective batch (.bat) files:
        To use this option first need to configure the path of conda activate application and replace it with the code in the file
        For Example for testing Login functionality double click on the file test_DPWorkLoginFunctionality.bat

    2. Using the Visual Studio Terminal:
        Click on Terminal option from the top of Visual Studio
        New Terminal
        From the dropdown select command prompt option
        Write the command to run respective testCases.

        Example: pytest -v testCases/test_dpwork_loginpage.py 
        Syntax: pytest -v testCases/{testCaseName}
