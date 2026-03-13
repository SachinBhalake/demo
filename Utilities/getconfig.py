import yaml


class ConfigReader:

    def __init__(self):
        with open("Config/config.yaml") as file:
            self.config = yaml.safe_load(file)

    def get_browser(self):
        return self.config["browser"]

    def get_grid_url(self):
        return self.config["grid_url"]

    def get_base_url(self, env):
        environments = self.config["environments"]

        if env not in environments:
            raise ValueError(
                f"Invalid env '{env}'. Available envs: {list(environments.keys())}"
            )
        return self.config["environments"][env]["base_url"]