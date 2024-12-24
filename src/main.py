import os
from utils.api_client import authenticate_user
from utils.url_parser import parse_login_endpoint
from utils.browser_handler import redirect_to_browser_with_url, redirect_to_browser_with_cookies

def main():
    platform_url = input("Enter the platform URL: ").strip()

    # Extract login endpoint
    login_url = parse_login_endpoint(platform_url)
    if not login_url:
        print("Invalid platform URL. Unable to determine login endpoint.")
        return

    # Authenticate programmatically
    email = os.getenv("USER_EMAIL")
    password = os.getenv("USER_PASSWORD")

    if not email or not password:
        print("Email or password is not set in .env.")
        return

    session_data = authenticate_user(login_url, email, password)
    if session_data:
        if "session_url" in session_data:
            redirect_to_browser_with_url(session_data["session_url"])
        elif "cookies" in session_data:
            redirect_to_browser_with_cookies(platform_url)
    else:
        print("Authentication failed or session data not available.")
