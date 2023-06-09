# Created by maksimdauhaleu at 5/20/23
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: BestSellers page test case
    Given Open Bestsellers Amazon page
    Then Verify there are 5 Bestseller links


Feature: Tests for bestsellers functionality

  Scenario: Bestsellers links can be opened
    Given Open Amazon Bestsellers
    Then User can click through top links and verify correct page opens