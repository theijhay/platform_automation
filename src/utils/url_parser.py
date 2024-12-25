from urllib.parse import urlparse

def parse_login_endpoint(url):
    """Generate a login endpoint based on the platform URL."""
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return f"https://{domain}/app/sign-in"
    except Exception as e:
        print(f"Error parsing URL: {e}")
        return None
