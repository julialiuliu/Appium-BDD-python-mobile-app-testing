import behave
import os
import sys

from time import sleep
from appium import webdriver

PAGE_NAVIGATION_TIMER    = 5
IDLE_TIMER               = 3

@behave.given('the app is launched')
def step_impl(context):
    try:
        context.reddit_home_page.skip_on_board_page()
        return
    except Exception as e:
        raise e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)

@behave.when(u'"{searchedterm}" is entered')
def step_impl(context, searchedterm):
    context.reddit_home_page.input_searched_term(searchedterm)
    sleep(IDLE_TIMER)
    context.reddit_home_page.send_enter_key()
    sleep(PAGE_NAVIGATION_TIMER)

@behave.then(u'should be able to see the "{searchedterm}" results')
def step_impl(context, searchedterm):
    assert context.reddit_home_page.check_searched_result_is_displayed(searchedterm) is True
    sleep(IDLE_TIMER)

@behave.when(u'tap on the "{searchedterm}" in the searched result list')
def step_impl(context, searchedterm):
    context.reddit_home_page.tap_on_the_searched_result(searchedterm)
    sleep(PAGE_NAVIGATION_TIMER)

@behave.then('should be able to save the most recent posted title')
def step_impl(context):
    assert context.reddit_home_page.save_top_posted_title_on_subreddit() is True
