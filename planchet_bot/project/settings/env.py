import os

from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_prefix = 'PLANCHET_'
        env_file_encoding = 'utf-8'
        env_file = os.getenv('ENV_PATH', 'conf/.env')
