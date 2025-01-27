# Web Scraping from CrisisWatch Tailor Made Project for UNICEF

* When I first see the task, I thought it can be handled with requests and BeautifulSoup libraries from python. 
    * If we only perform 1 page scraping without any dynamic page openings or filterings.

* When the html_parser is runned, I got 403 html code which depicts forbidden operation. 
    * In order to move with these workflow structure the correct html code should be returned as 200.
    * I wanted to print the 403 html code to see what is the real problem behind the scenes and saw that CloudFlare protection for CrisisWatch website.


* If we have this situation then we should mimic the browser behavior.
    * The solution that I knew was Selenium library.

* There is one popular documentation of Selenium library to see because it is generally updating with new subprocesses.

    * [Selenium Doc. Link](https://selenium-python.readthedocs.io/index.html)


* The task includes no additional files into the last version of script so I thought using webdriver of Selenium library to mimic the browser.

* There are several bottlenecks if we are using Selenium with Python.

* If you run this script locally, the general error that I encountered too is this (specific on Windows Operating System):


```
OSError: [WinError 193] %1 is not a valid Win32 application
```
    * There are different solutions for this problem depending on your local libraries and python version of course.
    * To solve it on my behalf, I checked these articles:

[Stackoverflow Article 1](https://stackoverflow.com/questions/25651990/oserror-winerror-193-1-is-not-a-valid-win32-application)

[Stackoverflow Article 2](https://stackoverflow.com/questions/78796828/i-got-this-error-oserror-winerror-193-1-is-not-a-valid-win32-application)


* For my system I downgraded Python version that I used in my virtual environment with VS Code.
    * Was using 3.12 and downgraded to 3.10 solved this error and allowed me to get .csv file into my local directory.
    * If user of this script wants to use it after Python version downgrade, requirements.txt is provided to install specific versions of the libraries which are needed.
    * Moreover, if we did not want to encounter these local problems Docker containers could be used for this task. If needed, I could provide Dockerfile for this project too.
 

# Thank You. ⚓
* Thank you for this task, I really enjoyed while performing.
    * Looking forward to meet the whole team and operate together in projects.

[LinkedIn](https://www.linkedin.com/in/erkutkoral/)
