#Author: Tirtha (raj) Subedi
# Code Challenge: Automate Allegiant Air site

# Software needed to install (visit: https://selenium-python.readthedocs.io/installation.html)
    - first, install Python bindings for Selenium (using: pip install selenium)
    - second, Download Driver for selenium (remember where it Downloaded) 
            download from: https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/
            or visit Driver Section on https://selenium-python.readthedocs.io/installation.html


# How to Run a Program?
    - After getting the code and installing the necessary software. 
    - Change the web driver path for the chrome driver (which is the path to where you downloaded chrome drive earlier). 
      {(Right-click on chrome driver and extract it. After that right-click on extracted chrome driver and copy its path then 
      past or replace the exsiting path on the code)}
    - After the chrome path has been changed, then you can run from a terminal using command: python main.py
      or from any IDE 
    - Once you execute a program, then it will start to automate through the Allegiant site by auto-filling all 
      the input fields.
    - Once automation is completed and the browser closed then you will see prices matched on the IDE output 
      or on the terminal.

 
# Additional info
   - Clone or download a program from Github
   - I have used time delay to give some time for Allegiant site to fully load 
   - Visit selenium-python for additional info if any errors occurred
   - It runs on both linux and mac
