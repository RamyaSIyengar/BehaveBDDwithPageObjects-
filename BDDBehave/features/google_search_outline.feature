
@smoke
Feature: Search feature
  Scenario Outline: Validating the search feature
    Given I navigate to google.com
    When I validate the page title
    Then I enter the text as "<searchTitle>"
    And I click on search button


    Examples:
      | searchTitle |
      | BDD         |
      | TDD         |


# behave features --tags=smoke
# behave features --tags=-smoke  => this will run other features apart from smoke

#  allure report
#  behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ features --tags=sanity
#  allure serve allure_reports

