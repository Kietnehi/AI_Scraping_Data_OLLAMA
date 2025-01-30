import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome browser...")

    # Path to ChromeDriver (Ensure it's the correct version for your Chrome browser)
    chrome_driver_path = r"C:\Program Files (x86)\chromedriver.exe"

    # Set Chrome Options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no UI)

    # Initialize WebDriver Service
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        print("Page Loaded....")
        time.sleep(5)  # Wait for content to load (can be improved with WebDriverWait)
        return driver.page_source
    finally:
        driver.quit()  # Ensure browser closes properly

def extract_body_content(html_content):
    """Extracts and returns the `<body>` content from the HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body_content):
    """Removes unnecessary `<script>` and `<style>` tags and returns cleaned text."""
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove scripts and styles
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    # Extract text content
    cleaned_content = soup.get_text(separator="\n")
    
    # Remove extra whitespace and empty lines
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome browser...")

    # Path to ChromeDriver (Ensure it's the correct version for your Chrome browser)
    chrome_driver_path = r"C:\Program Files (x86)\chromedriver.exe"

    # Set Chrome Options
    options = Options()

    # Initialize WebDriver Service
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        print("Page Loaded....")
        time.sleep(5)  # Wait for content to load (can be improved with WebDriverWait)
        return driver.page_source
    finally:
        driver.quit()  # Ensure browser closes properly

def extract_body_content(html_content):
    """Extracts and returns the `<body>` content from the HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body_content):
    """Removes unnecessary `<script>` and `<style>` tags and returns cleaned text."""
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove scripts and styles
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    # Extract text content
    cleaned_content = soup.get_text(separator="\n")
    
    # Remove extra whitespace and empty lines
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_dom_content(dom_content,max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)
    ]