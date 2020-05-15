# Import of Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from datetime import datetime
import time


# Bool for ending the loop
reviewFound = False


def wait(x):
    # Waiting will be needed at a few points in the script
    time.sleep(x)


def get_title_text():
    # Take some time for the elements to be loaded
    wait(1.5)
    title = driver.find_elements_by_tag_name("h1")
    return title


def fill_with_stars():
    x = 4
    buttonLine = driver.find_elements_by_class_name("button-star")
    buttonLine[x].click()
    buttonLine[x+5].click()
    buttonLine[x+10].click()
    buttonLine[x+15].click()
    buttonLine[x+20].click()
    buttonLine[x+25].click()
    wait(1)


def whats_this_card_about():
    # Choose the first option if required
    pass


def skip_or_wait(element):
    # If skippable - skip / If not - wait
    if element.is_enabled():
        element.click()
        wait(2)
    else:
        print("Element is not clickable. Waiting for timeout...")
        # At this time the timeout takes 20 minutes (1200s) to happen
        wait(600)

        # Go to the next Review by reloading
        # driver.get("https://wayfarer.nianticlabs.com/review")
        # wait(1)


def rate_or_skip(titleTexts, yourDesiredTitle):
    for text in titleTexts:
        print("Title of the current review: " + text.text)
        # If the text is the one we searched for
        if text.text == yourDesiredTitle:
            print("Giving it 5 Stars...")

            # Click 5 stars everytime
            fill_with_stars()

            # !!! Check if submitable - if not: Do whats_this_card_about

            # Click: submit
            submit = driver.find_elements_by_class_name("submit-btn-container")
            wait(1)
            # It is always the second element - could be done nicer
            submit[1].click()
            wait(1)

            # Setting Bool
            reviewFound = True

            # Go to the next Review by reloading
            driver.get("https://wayfarer.nianticlabs.com/review")
            wait(1)
        else:
            print("Skipping to next review or waiting for timeout...")
            # Click: skip review
            skip = driver.find_elements_by_class_name("button-secondary")
            # It is always the 4th element - could be done nicer
            skip_or_wait(skip[3])


def setup():
    # Set up options used by the chrome instance
    options = webdriver.ChromeOptions()
    # option.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    # Those options are the clue to pass Google's check if an automation software is used
    # Path to a chrome profile where you are already logged in to your google account is needed
    options.add_argument(
        "--user-data-dir=C:/Users/Joachim/AppData/Local/Google/Chrome/User Data")
    options.add_argument("--profile-directory=Profile 3")

    # Pass the path to the chromedriver as well as the defined options
    driver = webdriver.Chrome(
        executable_path='./chromedriver', options=options)

    # Start the chrome instance with the given website
    driver.get("https://wayfarer.nianticlabs.com/")

    # Click the first button you find
    loginElement = driver.find_elements_by_tag_name("button")
    loginElement[0].click()

    # Switch to the review page
    driver.get("https://wayfarer.nianticlabs.com/review")

    return driver


while not reviewFound:
    try:
        # Start the Browser instance
        driver = setup()
        # Show current time
        print(datetime.today().strftime('%d-%m-%Y / %H:%M:%S'))

        # Get text of the title section
        titleTexts = get_title_text()

        # Check if it is the review we searched for and rate it or skip if not
        rate_or_skip(titleTexts, "Uhr der Victoria Station")

        # Closing the browser
        driver.close()
    except KeyboardInterrupt:
        print("Program stopped! - See you soon :)")
        exit()


print(">>> Yes! Your Review has been found! <<<")
