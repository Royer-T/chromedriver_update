#  import packages (modules/classes)
import local_chrome

# we need to know about the Chrome that is installed locally (windows)
installed_chrome = local_chrome.installed_chrome.Chrome
installed_major_version = installed_chrome.chrome_major_version()

print(f'major installed version: {installed_major_version}')












