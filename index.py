from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

def download_instagram_video(url):
    try:
        print("Loading...")
        # Setup Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.

        # Open the browser and navigate to the URL
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url)
        time.sleep(5)  # Wait for the page to load

        # Extract video URL
        video_url = browser.find_element(By.CSS_SELECTOR, "video").get_attribute('src')

        # Download the video using requests
        if video_url:
            response = requests.get(video_url, stream=True)
            response.raise_for_status()
            with open('instagram_video.mp4', 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print("Video downloaded successfully.")
        else:
            print("Video URL not found.")

        # Close the browser
        browser.quit()

    except Exception as e:
        print(f"An error occurred: {e}")
        browser.quit()


# Hardcoded URL
instagram_video_url = input("Enter Video URL: ")

# Download the video
download_instagram_video(instagram_video_url)
