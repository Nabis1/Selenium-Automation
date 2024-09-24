from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://idos.cz/vlakyautobusymhdvse/spojeni/")

try:
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#didomi-notice-agree-button"))
    )
    cookie_button.click()
    print("Cookies accepted.")
except Exception as e:
    print(f"An error occurred: {e}")

timetable_button = driver.find_element(By.ID, "timetablesModalLink")
timetable_button.click()

current_url = driver.current_url
print(f"Current URL after click: {current_url}")

try:
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Český Těšín']"))
    )
    link.click()
    print("Clicked on Český Těšín link.")

except Exception as e:
    print(f"An error occurred: {e}")

current_url = driver.current_url
print(f"Current URL after click Český Těšín: {current_url}")

try:
    spojeni_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'conn-shield') and strong[text()='Spojení']]"))
    )
    spojeni_link.click()
    print("Clicked on Spojení link.")
except Exception as e:
    print(f"An error occurred while clicking the Spojení link: {e}")

current_url = driver.current_url
print(f"Current URL after clicking Spojení: {current_url}")

try:
    from_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "From"))
    )
    from_input.click()  
    from_input.clear()
    text_to_type = "Český Těšín,Svibice,Slovenská"
    from_input.send_keys(text_to_type)  
    print(f"Typed into the input field : {text_to_type}")
except Exception as e:
    print(f"An error occurred while typing into the input field: {e}")

try:
    to_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "To"))
    )
    
    to_input.click()  
    to_input.clear()  
    text_to_type = "Český Těšín,,aut.st."
    to_input.send_keys(text_to_type)  
    to_input.click()
    print(f"Typed into the input field : {text_to_type}")
except Exception as e:
    print(f"An error occurred while typing into the input field: {e}")

try:
    # Locate the checkbox using the label's `for` attribute
    checkbox_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='OnlyDirect']"))
    )
    checkbox_label.click()  # Click the label to toggle the checkbox
    print("Clicked the 'Pouze přímá spojení' checkbox.")
except Exception as e:
    print(f"An error occurred while clicking the 'Pouze přímá spojení' checkbox: {e}")


driver.quit()
