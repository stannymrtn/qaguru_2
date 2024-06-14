from selene import browser, be, have


def test_search(browser_driver):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_empty_search(browser_driver):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type("jkhfkdgwwww").press_enter()
    browser.element('#botstuff').should(have.text('По запросу jkhfkdgwwww ничего не найдено'))
