# Dependencies


    Python 3.x

    Selenium WebDriver

    Web driver for the chosen browser (Chrome or Firefox)
    

# Installation

- Clone the repository or download the script.

- Install the required dependencies by running the following command:

  `pip install selenium`

- Download the appropriate web driver for your browser and add it to your system's ***PATH***. Refer to the [Selenium documentation](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/) for detailed instructions on driver installation.

# Usage


- Open the terminal or command prompt.
  
  
- Navigate to the directory where the script is located.
  

- Run the script with the following command:

`python  whatsapp_security_test.py `


- The script will execute security testing on the WhatsApp Web application using the Firefox browser by default.


- To specify a different browser, use the --browser argument followed by the browser name ***(chrome or firefox):***
  

`python whatsapp_security_test.py --browser chrome`
  

- The script will display console logs, identify suspicious elements, and report suspicious network requests.


# Possible Errors and Fixes


- ***WebDriverException: 'geckodriver' executable needs to be in PATH:*** This error occurs when the geckodriver executable for Firefox is not in your system's PATH.
  
- Make sure you have downloaded the correct version of geckodriver and added its location to the PATH environment variable.


- ***SessionNotCreatedException:  Unable to find a matching set of capabilities:*** This error occurs when the web driver version does not match your browser version.

- Update the web driver to a compatible version or download the appropriate web driver for your browser.


- ***NoSuchElementException:*** This error occurs when the script fails to locate a web element.

- Verify that the web page structure has not changed and update the element locator strategy ***(e.g., using XPath instead of CSS selectors) in the script if necessary.***


If you encounter any other errors or issues, please refer to the Selenium documentation or search for solutions specific to your problem.


# Contributing

Contributions to the script are welcome! 

