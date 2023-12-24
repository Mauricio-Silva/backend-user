from urllib.parse import quote_plus
from contextvars import ContextVar
from dotenv import load_dotenv
from os import getenv
import sys


load_dotenv()


PREFIX = "/backend-user/api"
CONTEXT_VAR = ContextVar("url", default=None)

APP_TITLE = "Backend-User"
APP_VERSION = "v1.0.0"
APP_SUMMARY = "A service to manage users' accounts experience"
APP_DESCRIPTION = """
<!-- cSpell:disable -->
Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso do Sul - Três Lagoas <br/>
Tecnologia em Análise e Desenvolvimento de Sistemas - TADS <br/>

**SnapCut** - Social media for sharing videos
"""

MONGODB_URI = getenv("MONGODB_URI")
PASSWORD = getenv("PASSWORD")

if MONGODB_URI is not None and PASSWORD is not None:
    MONGODB_URI = MONGODB_URI.replace("<password>", quote_plus(PASSWORD))

DATABASE = getenv("DATABASE")
COLLECTION = getenv("COLLECTION")

EMAIL_SERVICE_BASE_URL = getenv("EMAIL_SERVICE_BASE_URL")
EMAIL_SERVICE_ACCESS_TOKEN = getenv("EMAIL_SERVICE_ACCESS_TOKEN")

SECRET_KEY = getenv("SECRET_KEY")
ACCESS_KEY = getenv("ACCESS_KEY")
ALGORITHM = getenv("ALGORITHM", "HS256")
CRYPTO_SCHEME = getenv("CRYPTO_SCHEME", "bcrypt")

EXPIRE_ACCESS_TOKEN_TIME = int(getenv("EXPIRE_ACCESS_TOKEN_TIME", 480))
EXPIRE_CHECK_ACCOUNT_TIME = int(getenv("EXPIRE_CHECK_ACCOUNT_TIME", 20))
EXPIRE_RESET_PASSWORD_TIME = int(getenv("EXPIRE_RESET_PASSWORD_TIME", 10))
