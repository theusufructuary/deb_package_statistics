# **deb_package_statistics**

## **Description**
Command line Python program that takes an architecture as an argument and then displays statistics of the top 10 Debian packages (by most associated files).

<br>

## _Note that this project is a work in progress which I am contributing to on an ad-hoc basis as a learning opportunity. I welcome any questions._

<br>

## **Linux Installation and Usage (development environment)**

**1).** To install on Linux (or Linux Subsystem for Windows), ensure you have git installed on your system, and then clone this repo via the terminal by running:

```
git clone https://github.com/theusufructuary/deb-package-statistics

cd deb-package-statistics

chmod 755 modules/package_statistics.py tests/test_package_statistics.py

```
>You may need to be a sudo user on your system to use 'chmod'.

<br>

**2).** To run the main project file, next enter:
```
cd modules

./package_statistics udeb-all

```

> Where 'udeb-all' is a command line argument. Valid arguments have to match a valid chip architecture as given on [the mirror this file is fetching data from](http://ftp.uk.debian.org/debian/dists/stable/main/) as seen on line 32 of the Python file.

<br>
<br>

## **Progress So Far**
- Understanding the problem and researching new concepts
- Repo & project management tools set up, plus initial project plan
- Stand up, write code, write/perform tests, code review, repeat, ending with a retro, including updated to documentation
- Implemented basic testing
- Solved problem with Python module imports

<br>

## **My Thought Process and Approach to the Problem**
#### **Agile**
As detailed in the Plan Overview section above, I structured my time around Agile working practices - plan design, code, test, review, repeat. 

#### **Computational Thinking**
I also used computational thinking to solve the problem by breaking the problem into smaller steps, focusing on what is important, and creating step-by-step instructions. This is evidenced in this project by the code plan which I wrote before writing even a single line of code in the package_statistics.py file, as well as the structure of my code. 

I tend to live by the phrase "writing code is expensive, writing a plan is cheap", alongside the understanding that a plan will never be perfect on the first iteration (hence my continued returning to previous parts of the task to amend and improve certain aspects).

#### **MVP**
I tried to achieve the minimum viable product (MVP) due to time constraints and to follow the fastest route to 'deploying' the project. For example, I came back to the issues I was having with printing package names in the console and the column alignment until later, because I had at least got it to print to terminal which was good enough to leave until after building other parts of the project.

I included some basic functionality for testing, logging, and error handling which I believe are minimum expected aspects of a project like this.

#### **Functions**
I also organised my project into functions, although I only officially declared them as functions later on in the project. One reflection I have is that I should have declared these functions at the beginning of the project. I typically do write code on a functional basis, but the learning curve I undertook to make this project made writing functionally hard at first. I would not do this in a production environment.

## **What would I do next?**
- With another two hours, I expect to have completed all the remaining tests I wrote in comments in the test file so there's a complete set of basic cautomated tests that check for correct functionality of the program.
- An additional hour would allow for enhancing the error handling for the program, ensuring other exceptions are covered by the program.
- Another two hours would give time for planning and improving the logging capabilities and coverage, exploring what would be useful as developers to log and where to send different log-level messages to.
- With another two hours, an additional argument could be given by the user to specify how many packages are printed to terminal
- Another 15 minutes would provide time for adding in column headings

## **Overall**
Overall I have thoroughly enjoyed the experience of making a command line package. At the same time as getting to use my SysAdmin and Developer knowledge to solve this, I've also learnt new skills! 

This project was my first time using argparse, urllib, and gzip modules in Python, as well as the first for me using a folder structure. The experience has made me even more eager to become a Python/SysAdmin guru and to create bigger, better, projects.

Thank you for your time.

<br>

## **Tech/Work Stack**

- Python 3
    - PIP
    - Flake8
    - Black
    - unittest

- IDE
    - VS Code

- Workflow
    - Github
    - Trello

- Misc
    - Manual testing in Ubuntu Shell
    - Documentation in Markdown
    - Internet for syntax and problem-solving assistance
    - I reached out to peers in tech if I needed assistance

