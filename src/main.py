import os
from utils.api_client import bypass_payment_check
from utils.url_parser import parse_login_endpoint
from utils.browser_handler import redirect_to_browser_with_url, redirect_to_browser_with_cookies
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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

    try:
        session_data = bypass_payment_check(platform_url, login_url, email, password)

        if not session_data:
            print("Authentication failed or session data not available.")
            return

        # Handle session data
        if "session_url" in session_data:
            print("Redirecting to session URL...")
            redirect_to_browser_with_url(session_data["session_url"])
        elif "cookies" in session_data:
            print("Redirecting using cookies...")
            redirect_to_browser_with_cookies(platform_url)
        else:
            print("Unknown session data format:", session_data)

    except Exception as e:
        print(f"An error occurred during the process: {e}")

if __name__ == "__main__":
    main()
