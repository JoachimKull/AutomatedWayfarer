from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from datetime import datetime
import random
import time
import sys
import time
import msvcrt

# Title of your submission
mySubmissions = ["title1", "title2"]

# Number of how many reviews the script will go through
dailyGoal = 36

# Bool for ending the loop
reviewFound = False


def load_review_page():
    driver.get("https://wayfarer.nianticlabs.com/review")
    wait(1)


def wait(x):
    # Waiting will be needed at a few points in the script
    time.sleep(x)


def get_title_text():
    # Take some time for the elements to be loaded
    wait(1.5)
    title = driver.find_elements_by_tag_name("h1")
    return title


def get_randN():
    return random.randint(2, 3)


# Safes the title of the current review to a file - only for statistics
def safe_title_to_file(titleString):
    try:
        text_file = open("reviewTitles.txt", "a")
        text_file.write("-" + titleString + "\n")
        text_file.close()
    except UnicodeEncodeError as unicodeEncodeError:
        print("Not saving this title to file, as it isn't encoded in unicode.")
    wait(1)


def click_submit():
    # Click: submit
    submit = driver.find_elements_by_class_name("submit-btn-container")
    wait(1)
    # Wait for a random amount of time (up to 2.5 minutes) to mime human behaviour
    x = random.randint(45, 150)
    print(
        "Waiting: " + str(x / 60) +
        " minutes before submitting to mime human behaviour"
    )
    wait(x)
    # It is always the second element - could be done nicer
    submit[1].click()
    wait(1)


# Fills every star field with a random number between 3 and 4
def fill_with_random_stars():
    buttonLine = driver.find_elements_by_class_name("button-star")

    buttonLine[get_randN()].click()
    buttonLine[get_randN() + 5].click()
    buttonLine[get_randN() + 10].click()
    buttonLine[get_randN() + 15].click()
    buttonLine[get_randN() + 20].click()
    buttonLine[get_randN() + 25].click()

    buttonLine = None
    wait(1)


# Fills every star field with 5 stars
def fill_with_five_stars():
    x = 4
    buttonLine = driver.find_elements_by_class_name("button-star")
    buttonLine[x].click()
    buttonLine[x + 5].click()
    buttonLine[x + 10].click()
    buttonLine[x + 15].click()
    buttonLine[x + 20].click()
    buttonLine[x + 25].click()

    buttonLine = None
    wait(1)


def whats_this_card_about():
    # Choose the first option if required
    cardHeaderTitles = driver.find_elements_by_class_name("card-header__title")

    # If last card found and it contains 'Required' press the first suggestion
    if cardHeaderTitles[8].text == "Worum handelt es sich?\n(Required)" or cardHeaderTitles[8].text == "What is it?\n(Required)":
        print("Selecting first suggestion because it is required")
        first_suggestion = driver.find_elements_by_tag_name("label")
        first_suggestion[0].click()


# Unfinished artefact
def choose_closest_position():
    pass


# Unfinished artefact
def choose_best_description():
    description = driver.find_elements_by_class_name(
        "known-information__description")
    print(description[0].text)
    pass


# If skippable - skip / If not - vote random
def skip_or_vote_random():
    skip = driver.find_elements_by_class_name("button-secondary")
    try:
        # It is always the 4th element - could be done nicer
        element = skip[3]
        if element.is_enabled():
            print("Skipping this submission")
            element.click()
            wait(2)
        else:
            print("Skip is not clickable. Doing the random vote.")
            # Fill every field
            fill_with_random_stars()

            # !!! Check if submitable - if not: Do - whats_this_card_about
            whats_this_card_about()

            # Submit
            click_submit()
    except IndexError:
        print("Something gone wrong, we will try it again...")


def rate_or_skip(titleTexts, myDesiredSubmissions):
    for text in titleTexts:
        print("Title of the current review: " + text.text)

        # Safe titles to file
        safe_title_to_file(text.text)

        for i in myDesiredSubmissions:
            # If the text is the one we searched for
            if text.text == i:
                print("Giving it 5 Stars...")

                # Click 5 stars everytime
                fill_with_five_stars()

                # !!! Check if submitable - if not: Do whats_this_card_about
                whats_this_card_about()

                # Submit
                click_submit()

                # Setting Bool accordingly
                reviewFound = True

                # Go to the next review by reloading
                load_review_page()
        else:
            print("Skipping to next review or do a random vote...")
            wait(1)
            # Click: skip review
            skip_or_vote_random()


def readInput(timeout):
    start_time = time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getche()
            if ord(chr) == 13:  # enter_key
                print("Enter pressed - Going to the next review")
                break
            elif ord(chr) >= 32:  # space_char
                input += chr
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break

    print('')  # needed to move to next line


def setup():
    # Set up options used by the chrome instance
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--disable-session-crashed-bubble")
    # Those options are the clue to pass Google's check if an automation software is used
    # Path to a chrome profile where you are already logged in to your google account is needed
    options.add_argument(
        "--user-data-dir=C:/Users/Joachim/AppData/Local/Google/Chrome/User Data")
    options.add_argument("--profile-directory=Profile 2")

    # Pass the path to the chromedriver as well as the defined options
    driver = webdriver.Chrome(
        executable_path="./chromedriver", options=options)

    # Start the chrome instance with the given website
    driver.get("https://wayfarer.nianticlabs.com/")

    # Click the first button you find
    loginElement = driver.find_elements_by_tag_name("button")
    loginElement[0].click()

    # Switch to the review page
    driver.get("https://wayfarer.nianticlabs.com/review")
    wait(1)

    return driver


for i in range(0, dailyGoal) or reviewFound:
    try:
        # Start the Browser instance
        driver = setup()

        # Show current time
        print("Date: " + datetime.today().strftime("%d-%m-%Y / %H:%M:%S"))

        # Get text of the title section
        titleTexts = get_title_text()

        try:
            # Check if it is the review we searched for and rate it or skip if not
            rate_or_skip(titleTexts, mySubmissions)
        except WebDriverException as driverException:
            print("We found a special case where human interaction is needed!")
            print("Press Enter if you resolved the case by yourself, else we will wait for the timeout (20 minutes): \n")
            # Wait for timeout or user input
            readInput(1200)

        # Closing the browser
        driver.quit()
    except KeyboardInterrupt:
        print("Program stopped! - See you soon :)")
        exit()

print(">>> Yes! Your Review has been found! ...or....OR! The limit has been reached: " +
      (str(dailyGoal-1)) + " <<<")
