from pathlib import Path

from planchet_bot.project.settings.env import EnvSettings

env = EnvSettings()

base_dir = Path(__file__).parent.parent.parent

TELEGRAM_BOT_TOKEN = env.TELEGRAM_BOT_TOKEN
