# deb_package_statistics

### Description
Command line Python program that takes an architecture as an argument and then displays statistics of the top 10 Debian packages (by most associated files).

<br>

### Plan Overview (with Time Management)
1st June - 1 hour - Understanding problem and research

*Long weekend holiday at EMF Festival*

6th June - 1 hour - Repo set up and initial project plan

7th June - 4 hours - Stand up, write code, write/perform tests, code review, repeat, ending with a retro, and any updates to documentation.

8th June - 1 hour - Contingency and submission of project.

<br>

### Code Plan
    # import required libs - urllib, argparse, requests, logger
    # receive command line arguments from user input
    # http get request to Debian mirror to create a local copy of Contents file of architecture requested by user
    # for loop to parse each line of the Contents file and count number of files associated with each package, storing results in an object
    # print names of the top 10 packages and the number of files associated with them, in descending order (largest printed first)

<br>

### Tech/Work Stack

- Python 3
    - PIP
    - Flake8
    - Black
    - unittest

- IDE
    - VS Code

- Workflow
    - Github

- Misc
    - Manual testing in Ubuntu Shell
    - Documentation in Markdown
