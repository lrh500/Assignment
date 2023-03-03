Feature: Rating
"""Confirm that we can browse the rating related page on our Site"""
Scenario:
    Given I navigate to teh rating pages
    When I click on the link to the rating details
    Then I should see the details for that movie