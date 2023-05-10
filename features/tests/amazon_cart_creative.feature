# Created by maksimdauhaleu at 5/10/23
Feature: Amazon Cart-Creative tests

  Scenario: User can search for table on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"
    Then Open an item and add to cart
    Then Check if the item is in a cart