from pathlib import Path

from planchet_bot.project.settings.env import EnvSettings

env = EnvSettings()

base_dir = Path(__file__).parent.parent.parent

TELEGRAM_BOT_TOKEN = env.TELEGRAM_BOT_TOKEN


WEATHER_LOCATION_LAT = env.WEATHER_LOCATION_LAT
WEATHER_LOCATION_LON = env.WEATHER_LOCATION_LON
WEATHER = {
    'api_token': env.WEATHER_API_TOKEN,
    'api_base_url': env.WEATHER_API_BASE_URL,
    'location_lat': env.WEATHER_LOCATION_LAT,
    'location_lon': env.WEATHER_LOCATION_LON,
}
