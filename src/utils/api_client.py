import requests
import pickle
from http.cookiejar import MozillaCookieJar

def authenticate_user(login_url, email, password):
    """Authenticate the user and return session data (URL or cookies)."""
    payload = {"email": email, "password": password}
    session = requests.Session()  # Maintain session for cookies

    try:
        response = session.post(login_url, json=payload)
        response.raise_for_status()
        
        data = response.json()
        print("Login successful!")

        # Handle session URL or cookies
        session_url = data.get("session_url")
        if session_url:
            print("Session URL found. Payment checks bypassed!")
            return {"session_url": session_url}
        else:
            # Save cookies if session URL is not provided
            save_cookies(session.cookies)
            print("Cookies saved for browser redirection.")
            return {"cookies": session.cookies}
    except requests.RequestException as e:
        print(f"Error during authentication: {e}")
        return None


def save_cookies(cookies):
    """Save cookies to a file for browser integration."""
    cookie_jar = MozillaCookieJar("cookies.txt")
    for cookie in cookies:
        cookie_jar.set_cookie(cookie)
    cookie_jar.save()
