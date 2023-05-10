# Created by maksimdauhaleu at 5/10/23
Feature: Amazon cart tests

  Scenario: Verifying user cart is empty
    Given Open amazon main page
    When Find cart button on the page
    Then Verify cart is empty

