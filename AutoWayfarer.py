# Import of Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Set up options used by the chrome instance
options = webdriver.ChromeOptions()
# option.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
# Those options are the clue to pass Google's check if an automation software is used
# Path to a chrome profile where you are already logged in to your google account is needed
options.add_argument(
    "--user-data-dir=C:/Users/Joachim/AppData/Local/Google/Chrome/User Data")
options.add_argument("--profile-directory=Profile 2")

# Pass the path to the chromedriver as well as the defined options
driver = webdriver.Chrome(
    executable_path='./chromedriver', options=options)

# Used for debugging purposes to get the session id of the chrome instance
#executor_url = driver.command_executor._url
#session_id = driver.session_id
# print(session_id)
# print(executor_url)

# Waiting - TBF!
driver.implicitly_wait(30)

# Start the chrome instance with the given website
driver.get("https://wayfarer.nianticlabs.com/")

# Click the first button you find
loginElement = driver.find_elements_by_tag_name("button")
loginElement[0].click()

# Switch to the review page
driver.get("https://wayfarer.nianticlabs.com/review")

# Get text of the title section
getTitle = driver.find_elements_by_class_name("title-description")
# getTitle[0].text
print(getTitle)

# Compare the text to a predefined one

""""loginElement = browser.find_elements_by_tag_name("button")
loginElement[0].click()

emailElement = browser.find_elements_by_tag_name("input")
emailElement[0].send_keys("joachim.kull94@googlemail.com")

confirmEmail = browser.find_elements_by_tag_name("button")
confirmEmail[0].click() """
