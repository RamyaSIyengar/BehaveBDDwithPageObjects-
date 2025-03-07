Feature: Registration Feature
  Scenario Outline: Validating the Registration Feature
    Given I navigate to qa.way2automation.com
    When I enter the name as "<name>"
    Then I enter the phone number as "<phoneNumber>"
    And I enter the email as "<email>"
    And I enter the country as "<country>"
    And I enter the city as "<city>"
    And I enter the username as "<username>"
    And I enter the password as "<password>"
    And I click on the submit button

    Examples:
      |name    |phoneNumber|email            |country|city |username|password|
      |Raju    |9129876565  |Raju@gmail.com  |India  |Delhi|Raj     |Raj@qwe |
      |Ram     |9178900211  |Ram@gmail.com   |India  |Mumbai|Ram     |Ram@123 |

#behave features

#     behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ features