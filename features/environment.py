import os
import sys

from appium import webdriver
from time import sleep
from utils.smart_driver import *

IDLE_TIMER    =  3
#Hooks
def before_all(context):
    context.config.setup_logging()
    driver_setup(context.config.userdata.get("appium_host", "unknown"),
                 context.config.userdata.get("appium_port", "unknown"),
                 context.config.userdata.get("appium_version", "unknown"),
                 context.config.userdata.get("platform_name", "unknown"),
                 context.config.userdata.get("platform_version", "unknown"),
                 context.config.userdata.get("device_name", "unknown"),
                 context.config.userdata.get("browser_name", "unknown"),
                 context.config.userdata.get("device_orientation", "unknown"),
                 context.config.userdata.get("test_name", "unknown"),
                 context.config.userdata.get("app_uri", "unknown"),
                 context.config.userdata.get("saucelabs_user", "unknown"),
                 context.config.userdata.get("saucelabs_key", "unknown"),
                 context.config.userdata.get("saucelabs_on", "unknown"))
    start_driver(context)

def after_all(context):
    #TODO
    #uninstall the app on cloude device
    #context.driver.remove_app(context.config.userdata.get("app_uri"));
    pass

def before_feature(context, feature):
    pass

def before_scenario(context, scenario):
    #start_activity()
    #Android ONLY
    #get_current_activity()
    pass

def after_scenario(context, scenario):
    #TODO
    pass

def after_feature(context, feature):
    cleanup_driver(context)

def before_step(context, step):
    pass

def after_step(context, step):
    take_screenshot(context, step.name)
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_file('screenshots\\{}.png'.format
                       (step.name)),
        name="Screenshot",
        attachment_type=AttachmentType.PNG)
        sleep(IDLE_TIMER)

def before_tag(context, tag):
    pass

def after_tag(context, tag):
    pass
