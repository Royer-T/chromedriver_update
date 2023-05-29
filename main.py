import winreg


# determine the version of the local version of Chrome
def get_chrome_version():
    """
    Retrieves the version of Google Chrome installed on the system.

    :return: Version of Google Chrome installed on the system.
    Returns None if Chrome is not installed or the registry key is not found.
    :rtype: str
    """
    try:
        # Open the registry key containing Chrome's version information
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")

        # Read the version value
        version, _ = winreg.QueryValueEx(reg_key, "version")

        return version
    except FileNotFoundError:
        # Handle the case when Chrome is not installed or the registry key is not found
        return None


# Call the function to get the Chrome version
chrome_version = get_chrome_version()

if chrome_version:
    print(f"Chrome version: {chrome_version}")
else:
    print("Chrome is not installed or the version couldn't be determined.")