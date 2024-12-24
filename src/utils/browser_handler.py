import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def redirect_to_browser_with_url(url):
    """Open the given URL in the default web browser."""
    try:
        print(f"Redirecting to browser with URL: {url}")
        webbrowser.open(url)
    except Exception as e:
        print(f"Failed to redirect to browser with URL: {e}")


def redirect_to_browser_with_cookies(platform_url):
    """Open the platform URL in a browser with cookies set."""
    try:
        # Setup browser options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        
        # Load cookies
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(platform_url)
        
        # Load saved cookies
        driver.delete_all_cookies()
        cookie_jar = "cookies.txt"  # Ensure cookies were saved
        driver.add_cookie_file(cookie_jar)
        
        print("Cookies loaded. You are now authenticated in the browser.")
        driver.refresh()  # Refresh to apply cookies
    except Exception as e:
        print(f"Failed to redirect with cookies: {e}")
