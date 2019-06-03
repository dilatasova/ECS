# Tech Assessment

## Setup
Requires Python 3.6+ (for f-strings) and selenium module, as well as a chrome install.
A requirements.txt file is included for ease of installation (> pip install -r requirements.txt).

To run, should just be able to execute from the command line (e.g. > python .\ta.py).
A Chromedriver.exe is included for convenience, but you can download the driver yourselves if you're understandably wary about running strange .exe files.
Chromedriver needs to be in the same directory if you want to avoid having to set PATH variables.

## Notes

* Used python for ease of setup (e.g. just one file rather than whole solution).
* Used inbuilt python unittest module for simplicity.
* Selenium test not written as I would normally like, as should really by using Page Object Model pattern for this sort of testing. Seemed like overkill for this exercise.