import yaml


class ConfigReader:

    _config = None
    VALID_BROWSERS = ["chrome", "firefox"]

    def __init__(self, env_override=None, browser_override=None, headless_override=False):

        if ConfigReader._config is None:
            with open("Config/config.yaml", encoding="utf-8") as file:
                ConfigReader._config = yaml.safe_load(file)

        self.config = ConfigReader._config

        # -------- ENV --------
        self.environments = self.config.get("environments", {})
        self.env = (env_override or self.config.get("env")).lower()

        if self.env not in self.environments:
            raise ValueError(f"Invalid env: {self.env}")

        # -------- BROWSER --------
        self.browser = (browser_override or self.config.get("browser")).lower()

        if self.browser not in self.VALID_BROWSERS:
            raise ValueError(f"Unsupported browser: {self.browser}")

        # -------- HEADLESS (CLI ONLY) --------
        self.headless = bool(headless_override)

    # -------- getters --------
    def get_env(self):
        return self.env

    def get_browser(self):
        return self.browser

    def is_headless(self):
        return self.headless

    def get_grid_url(self):
        return self.config.get("grid_url")

    def get_ui_base_url(self):
        return self.environments[self.env]["ui_base_url"]

    def get_api_base_url(self):
        return self.environments[self.env]["api_base_url"]