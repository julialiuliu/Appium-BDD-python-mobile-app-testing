# Appium-BDD-python-mobile-app-testing

#####################################
#  Run Automation Script            #
#####################################
#debugging
behave features/search.feature --no-capture -f plain


#####################################
#  Run and GUI Report               #
#####################################
# -- ALLURE-FORMATTER REQUIRES:
# ALLURE_REPORTS_DIR=allure.reports
# behave -f allure -o $ALLURE_REPORTS_DIR ...
# allure serve $ALLURE_REPORTS_DIR

#Allure reports
behave -f allure_behave.formatter:AllureFormatter -o ./reports/report/ ./features/
allure serve ./reports/report/
