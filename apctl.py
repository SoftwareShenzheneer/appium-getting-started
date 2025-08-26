from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android",
        "automationPackage": "app.revanced.android.youtube",
        "appActivity": "com.google.android.youtube.app.honeycomb.Shell$HomeActivity",
        "language": "en",
        "locale": "US"
        }

# options = UiAutomator2Options().load_capabilities({
#     "platformName": "Android",
#     "automationName": "UiAutomator2",
#     "deviceName": "Android",
#     "appPackage": "app.revanced.android.youtube",
#     "appActivity": "com.google.android.youtube.app.honeycomb.Shell$HomeActivity",
#     "language": "en",
#     "locale": "US"
# })

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android"
options.app_package = "app.revanced.android.youtube"
options.app_activity = "com.google.android.youtube.app.honeycomb.Shell$HomeActivity"
options.language = "en"
options.locale = "US"
options.auto_grant_permissions = True
options.skip_device_initialization = True
options.skip_server_installation = True

serverUrl = "http://127.0.0.1:4723"

# driver = webdriver.Remote(serverUrl, caps)
driver = webdriver.Remote(command_executor=serverUrl, options=options)

input()
driver.quit()

