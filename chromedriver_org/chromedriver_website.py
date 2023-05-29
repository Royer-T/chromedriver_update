import logging
import requests

#  set the logging behaviour
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s '
                                               '- %(name)s:%(message)s')
logger = logging.getLogger(__name__)


class Chromedriver:
    @staticmethod
    def get_latest_chromedriver_version():
        """
        Retrieve the latest version of ChromeDriver.

        This method makes a network request to the ChromeDriver website
        to fetch the latest version of ChromeDriver. The version number
        is extracted from the response and returned as a string.

        :return: The latest version of ChromeDriver.
        :rtype: str
        :raise: requests.exceptions.RequestException: If a network error occurs
        during the request.
        """
        chrome_driver_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"

        try:
            response = requests.get(chrome_driver_url)

            # Raise an exception for non-2xx status codes
            response.raise_for_status()

            latest_version = response.text.strip()

            return latest_version
        except requests.exceptions.RequestException as e:
            logger.error(f'Error occurred during the request: {e}')
            raise
