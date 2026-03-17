import yaml


class ConfigReader:

    _config = None

    def __init__(self):
        if ConfigReader._config is None:
            with open("Config/config.yaml", encoding="utf-8") as file:
                ConfigReader._config = yaml.safe_load(file)

        self.config = ConfigReader._config

    def get_browser(self):
        return self.config.get("browser")

    def get_grid_url(self):
        return self.config.get("grid_url")

    def get_base_url(self, env):
        environments = self.config.get("environments", {})

        if env not in environments:
            raise ValueError(
                f"Invalid env '{env}'. Available envs: {list(environments.keys())}"
            )

        return environments[env]["base_url"]