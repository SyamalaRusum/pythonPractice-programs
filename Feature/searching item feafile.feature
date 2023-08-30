Feature: Search
  Scenario Outline: textbox is present in search page
    Given open the browser
    When load the url
    Then search for <item>
    And close the browser
    Examples:
      | item |
    |flowers|



