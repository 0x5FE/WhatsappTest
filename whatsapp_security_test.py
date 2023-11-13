import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_whatsapp_web(browser='chrome'):
    allowed_browsers = ['chrome', 'firefox']
    
    if browser not in allowed_browsers:
        raise ValueError("Unsupported browser. Use 'chrome' or 'firefox'.")
    
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-infobars')  
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    
    return driver  

def security_testing(browser='chrome'):
    driver = open_whatsapp_web(browser)  

    if driver:
        try:
            if browser == 'chrome':
                console_logs = driver.get_log('browser')
            elif browser == 'firefox':
                console_logs = driver.get_log('driver')
            
            print("Console Logs:")
            for log_entry in console_logs:
                print(log_entry)
            
            suspicious_elements = driver.find_elements(By.CSS_SELECTOR, '.suspicious-element-class')
            if suspicious_elements:
                print(f"Suspicious elements found: {len(suspicious_elements)}")
                for element in suspicious_elements:
                    print(f"Suspicious Element: Tag={element.tag_name}, ID={element.get_attribute('id')}")
            
            network_requests = driver.execute_script("return window.performance.getEntries();")
            for request in network_requests:
                if 'suspicious-url' in request['name']:
                    print(f"Suspicious network request: {request['name']}")
                    print(f"Charging Time: {request['duration']} ms")
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        finally:
            driver.quit()
    else:
        print("Failed to open WhatsApp Web.")

def main():
    security_testing(browser='firefox')

if __name__ == "__main__":
    main()
