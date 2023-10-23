from . import env


FASTAPI = dict(
    title=env.APP_TITLE,
    summary=env.APP_SUMMARY,
    description=env.APP_DESCRIPTION,
    version=env.APP_VERSION,
    docs_url="/"
)

ALLOW_ORIGINS = [
    "http://127.0.0.1:8000/docs"
]

ORIGIN = dict(
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Server:
    app = FASTAPI
    origin = ORIGIN


ENVS = (
    env.DB_NAME,
    env.COLLECTION_NAME,
    env.SECRET_KEY,
    env.EMAIL_SERVICE_BASE_URL,
    env.EMAIL_SERVICE_ACCESS_TOKEN
)
DB_ENVS = (
    env.DB_SERVER,
    env.DB_USER,
    env.DB_PASSWORD,
    env.DB_CLUSTER,
    env.DB_DOMAIN
)


class Lifespan:
    envs = ENVS
    db_envs = DB_ENVS
    docker = env.DOCKER_URI
    mongo = env.MONGO
    browser = env.BROWSER
    SWAGGER = env.SWAGGER


class JWT:
    secret = env.SECRET_KEY
    algorithm = env.ALGORITHM
    expire = env.EXPIRE_TIME
    scheme = env.CRYPTO_SCHEME


class Email:
    base_url = env.EMAIL_SERVICE_BASE_URL
    access_token = env.EMAIL_SERVICE_ACCESS_TOKEN
