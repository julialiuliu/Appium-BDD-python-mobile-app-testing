### Appium-BDD-python-mobile-app-testing

#### This is a smoke test for Reddit App

1. Launch the Reddit App on local device
2. Search for a subreddit called "gaming"
3. Open the sub-reddit
4. Printout the top most post's title

#### TODO
1. Integrate to cloud test farm (ex:Amazon test farm or Sourcelabs)
2. Send out output report to emailbox
3. Integrate to Jenkin or Bamboo

####How to run this script

Option 1. Run the script
behave ./features/ --no-capture -f plain


Option 2. Run the script and generate Allure report

behave -f allure_behave.formatter:AllureFormatter -o ./reports/report/ ./features/

allure serve ./reports/report/
