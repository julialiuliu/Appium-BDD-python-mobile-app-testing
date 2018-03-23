# Appium-BDD-python-mobile-app-testing

Option 1. Run the script
behave ./features/ --no-capture -f plain


Option 2. Run the script and generate Allure report

#Allure reports

behave -f allure_behave.formatter:AllureFormatter -o ./reports/report/ ./features/

allure serve ./reports/report/
