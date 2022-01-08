from typing import Any

from . import config as config_module


class Settings:
    def __init__(self) -> None:
        for setting in dir(config_module):
            if setting.isupper():
                setting_value = getattr(config_module, setting)

                setattr(self, setting, setting_value)

    # To pass mypy type checking
    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)


settings = Settings()
