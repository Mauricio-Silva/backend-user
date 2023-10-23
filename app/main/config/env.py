from dotenv import load_dotenv
from urllib.parse import quote_plus
from os import getenv
import sys


load_dotenv()


PREFIX = "/snapcut/api"
APP_TITLE = getenv("APP_TITLE", "FastAPIApp")
APP_PORT = int(getenv("APP_PORT", 8000))
APP_VERSION = getenv("APP_VERSION", "v1.0")
APP_SUMMARY = getenv("APP_SUMMARY", "summary")
APP_DESCRIPTION = getenv("APP_DESCRIPTION", "description")

if APP_DESCRIPTION.startswith("path:"):
    with open(APP_DESCRIPTION.removeprefix("path:")) as file:
        APP_DESCRIPTION = file.read()

DB_SERVER = getenv("DB_SERVER")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_CLUSTER = getenv("DB_CLUSTER")
DB_DOMAIN = getenv("DB_DOMAIN")
DB_NAME = getenv("DB_NAME")
COLLECTION_NAME = getenv("COLLECTION_NAME")

DOCKER_URI = getenv("DOCKER_URI")
DB_URL = "{server}://{user}:{password}@{cluster}.{domain}"
DB_URI = DB_URL.format(
    server=DB_SERVER,
    user=DB_USER,
    password=quote_plus(DB_PASSWORD),
    cluster=DB_CLUSTER,
    domain=DB_DOMAIN
)

MONGO = DB_URI if not DOCKER_URI or not len(DOCKER_URI) else DOCKER_URI
EMAIL_SERVICE_BASE_URL = getenv("EMAIL_SERVICE_BASE_URL")
EMAIL_SERVICE_ACCESS_TOKEN = getenv("EMAIL_SERVICE_ACCESS_TOKEN")

BROWSER = getenv("BROWSER", "google-chrome")
HOST = "0.0.0.0" if "--host" in sys.argv else "127.0.0.1"
SWAGGER = f"http://{HOST}:{APP_PORT}/docs"

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM", "HS256")
EXPIRE_TIME = int(getenv("EXPIRE_MINUTES_TIME", 120))
CRYPTO_SCHEME = getenv("CRYPTO_SCHEME", "bcrypt")
