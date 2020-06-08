# AutomatedWayfarer
This is a Python Script based on Selenium for **automated searching through the Pokemon Go's Wayfarer Portal**. The goal is to find a certain review (or multiple) based on the title to give it a certain rating.

The script is by far not a perfect masterpiece, because it doesn't handle all special cases and it doesn't use xpath -> Therefore feel free to place a merge request.

## Prerequisites
Download: 
- [Python 3](https://www.python.org/downloads/) and add it to PATH
- the [chromedriver](https://chromedriver.chromium.org/downloads)
- and the [chrome browser version 83](https://www.google.com/chrome/) itself

In the browser - log in and activate sync - restart and see if sync is paused. 

If sync is still paused type ```chrome://settings/content/cookies``` into the search bar and whitelist ```accounts.google.com``` - Syncing should work now.
- Open up a command prompt in the folder of this script and  
```
pip install selenium
```

## Usage
- Open up the ```AutoWayfarer.py``` file in a text editor and change the name of the submissions (```mySubmissions = ["title1", "title2"]```) you want to search for, then safe and close.
- In your opened command prompt type:

```
python ./AutoWayfarer.py
```
- To stop the script from running press ```Control + C```

### TODO

- [ ] Refactor using xpath?

*Special cases are somewhat handled with a timeout to move on and to not break the script*

- [ ] Special cases:
  - [ ] Determine closest position
  - [ ] Determine best titel
  - [x] "What is this card about (Required)" (h4 class: card-header__title) -> needs to be chosen