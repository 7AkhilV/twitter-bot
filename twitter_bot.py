from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def post_tweet(username, password, message):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--force-device-scale-factor=1')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)
    
    try:
        # Login to Twitter
        driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        
        # Enter username
        username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
        username_field.send_keys(username)
        username_field.send_keys(Keys.RETURN)
        time.sleep(2)
        
        # Enter password
        password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # Click compose tweet button (using the blue button)
        compose_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="SideNav_NewTweet_Button"]')))
        driver.execute_script("arguments[0].click();", compose_button)
        time.sleep(3)
        
        # Enter tweet text using clipboard
        tweet_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
        driver.execute_script("""
        const text = arguments[0];
        const dataTransfer = new DataTransfer();
        dataTransfer.setData('text', text);
        const event = new ClipboardEvent('paste', {
            clipboardData: dataTransfer,
            bubbles: true
        });
        arguments[1].dispatchEvent(event);
        """, message, tweet_input)
        time.sleep(2)
        
        # Click tweet button
        tweet_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))
        driver.execute_script("arguments[0].click();", tweet_button)
        time.sleep(5)  # Wait longer to ensure tweet is posted
        
        print("Tweet posted successfully!")
        return True
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False
    finally:
        time.sleep(5)  # Wait before closing to see what happened
        driver.quit()
