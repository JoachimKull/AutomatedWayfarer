# AutomatedWayfarer
This is a Python Script based on Selenium for automated searching through the Pokemon Go's Wayfarer Portal. The goal is to find a certain review based on the title to give it a certain rating.

## Prerequisites
- Download Python 3 and add it to PATH
- Download: The [chromedriver](https://chromedriver.chromium.org/downloads)
- The [chrome browser](https://www.google.com/chrome/) itself
- In the browser - log in and activate sync - restart and see if it is sync is paused. If so type ```chrome://settings/content/cookies``` into the search bar and whitelist ```accounts.google.com```. Syncing should now work.
- Open up a command prompt in this folder and 
```
pip install selenium
```

## Usage
- In your opened command prompt type:

```
python ./AutoWayfarer.py <path-to-your-chrome-user-directory> <path-to-your-used-profile> <title-of-the-searched-review>
```
- To stop the script from running press ```Control + C```

### TODO
- [ ] Setup arg parsing

- [ ] Terminate gracefully?

- [ ] Refactor in methods for reusability

- [x] Run it in loop

- [x] Skip to next review -> done by reloading the page

- [x] Wait for timeout -> func

- [x] Give 5 stars if it is your searched review -> func

- [ ] Special cases: 
  - Determine closest position
  - "What is this card about (Required)" (h4 class: card-header__title) -> needs to be chosen