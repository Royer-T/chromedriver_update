from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER


class Chrome:
    @staticmethod
    def chrome_version():
        """
        Retrieves the version of Google Chrome installed on the system.

        This method accesses the Windows registry using the `winreg` module to
        retrieve the version information of Google Chrome. It looks for the
        registry key containing Chrome's version information and retrieves the
        version value. If Chrome is not installed or the registry key is not
        found, it returns None.

        :return: Version of Google Chrome installed on the system.
         Returns None if Chrome is not installed or the registry key is not found.
        :rtype: str or None
        """
        try:
            with OpenKey(HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon") as reg_key:
                version, _ = QueryValueEx(reg_key, "version")
                return version
        except FileNotFoundError:
            # Handle the case when Chrome is not installed
            # or the registry key is not found
            return None

    @staticmethod
    def chrome_major_version():
        """
        Retrieves the major version of Google Chrome installed on the system.

        This method retrieves the complete version of Google Chrome using the
        `chrome_version()` static method and then extracts the major version
        by finding the index of the dot (.) separator. The major version
        represents the numerical portion of the version string before the dot.

        :return: The major version of Google Chrome installed on the system.
        :rtype: str
        """
        complete_version = Chrome.chrome_version()

        try:
            major_version = complete_version.split('.', 1)[0]
            return major_version
        except IndexError:
            # Handle the case where the version string does not contain a dot
            # separator
            return complete_version

        return installed_major_chrome_version
