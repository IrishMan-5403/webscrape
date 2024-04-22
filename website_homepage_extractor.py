from selenium import webdriver
import re 
import os
url ="https://www.google.com/"
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
driver.get(url)

# Define the folder where screenshots will be saved
screenshot_folder = "website_screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

# List of websites to visit
websites = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.github.com"
]
    # Add more websites as needed
# Loop through each website
for index, website in enumerate(websites, start=1):
    try:
        # Open the website
        driver.get(website)

        # Get the title of the webpage (for file naming)
        title = driver.title.strip().replace(" ", "_")

        # Take a screenshot and save it in the screenshot folder
        screenshot_path = os.path.join(screenshot_folder, f"{index}_{title}.jpg")
        driver.save_screenshot(screenshot_path)

        print(f"Screenshot saved: {screenshot_path}")

    except Exception as e:
        print(f"Error processing {website}: {str(e)}")

# Quit the WebDriver
driver.quit()
