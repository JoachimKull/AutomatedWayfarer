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
python ./AutoWayfarer.py
```
- To stop the script from running press ```Control + C```

### TODO

- [X] Terminate gracefully?

- [x] Refactor in methods for reusability

- [x] Run it in loop

- [x] Skip to next review -> done by reloading the page

- [x] Wait for timeout -> func

- [x] Give 5 stars if it is your searched review -> func

- [ ] Add random number gen. for generating numbers between 3 and 4
  
- [ ] Safe titles of reviews in file to see which type happens the most
  
- [ ] Set flexible limit (35) of 'daily' reviews done by the script + random time between the reviews
  
- [ ] Change behaviour to always vote the submission and if the ones we searched for are found do the 5 stars -> new branch

- [ ] Special cases:
  - Check for City/s and give 5 Stars 
  - Determine closest position
  - "What is this card about (Required)" (h4 class: card-header__title) -> needs to be chosen