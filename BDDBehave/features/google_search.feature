@sanity
Feature: Search feature

  Background:
    Given I navigate to google.com


  Scenario: Validating the search feature
    When I validate the page title
    Then I enter the text as "hello selenium"
    And I click on search button


  Scenario: Validating the search feature with new text
    When I validate the page title
    Then I enter the text as "behave"
    And I click on search button
