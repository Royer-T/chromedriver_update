import logging

#  import packages (modules/classes)
import chromedriver_org
import local_chrome

# 1. we need to know about the Chrome that is installed locally (windows)
installed_chrome = local_chrome.installed_chrome.Chrome
installed_major_version = installed_chrome.chrome_major_version()

print(f'Installed Chrome version: {installed_chrome}')
print(f'Installed Chrome major version: {installed_major_version}')

# 2. we need to know about the latest chromedriver version available at:
download_chromedriver = chromedriver_org.chromedriver_website.Chromedriver
latest_stable_version = download_chromedriver.get_latest_chromedriver_version()

print(f'latest chromedriver available: {latest_stable_version}')


print('we are here')
















