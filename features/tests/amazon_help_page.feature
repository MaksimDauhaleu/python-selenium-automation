# Created by maksimdauhaleu at 6/4/23
Feature: Test for window switch with Selenium

Scenario: User can open and close Amazon Privacy Notice
Given Open Amazon T&C page
When Store original windows
And Click on Amazon Privacy Notice link
And Switch to the newly opened window
Then Verify Amazon Privacy Notice page is opened
And User can close new window and switch back to original