Hi! The goal this documentation is give some information about the structurs.

Test objects are: calculator.py and icalc.py.

In the "test" forlder you can find some python file. The test files are starting with "test_" and after that the operation what the test is checking in the calculator, for example, add, multiply etc.

Furthermore the test folder contains 2 other python files: conftest and generator.

The generator.py can generate random datas to the tests.

The conftest.py contains the settings of the pytest. In this file, I gave 2 option, what you can use when you would like to execute the test, these options: key, calculator. With "key" option you can execute specific test case
for example if you would like to check the calculator's operation with integer only with this option you can do it. Example:

pytest .\test_sub.py --key robust

The other option is the "calculator". If you would like to texecute the test on the interactive calculator give the following:
pytest .\test_sub.py --calculator i_cal

If you give anything after the "--calculator" it will cause test execution on icalc (interactive calculator), because by default the simple calculator is tested, so the "--calcultor" was set to the calculator.

In the "results" folder you can find the results of the test execution.

The bugs.txt contains the found bugs.

