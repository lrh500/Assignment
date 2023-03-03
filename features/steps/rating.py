from behave import given,when,then

@given (u'I navigate to the rating pages')
def nav(context):
    context.browser.get('https://arcticsaddle-jumbofloat-5000.codio-box.uk/')

@when (u'I click on the link to rating details')
def click(context):
    context.browser.find_element_by_partial_link_text('2').click()

@then (u'I should see the rating details for the movie')
def details(context):
    print(context.browser.page_source)
    assert context.browser.current_url=='https://arcticsaddle-jumbofloat-5000.codio-box.uk/rating_details/2'
    assert '1045 3 5.5' in context.browser.page_source