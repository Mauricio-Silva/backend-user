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
    env.DB_SERVER,
    env.DB_USER,
    env.DB_PASSWORD,
    env.DB_CLUSTER,
    env.DB_DOMAIN,
    env.DB_NAME,
    env.COLLECTION_NAME,
    env.SECRET_KEY
)


class Lifespan:
    envs = ENVS
    mongo = env.MONGO
    browser = env.BROWSER
    SWAGGER = env.SWAGGER


class JWT:
    secret = env.SECRET_KEY
    algorithm = env.ALGORITHM
    expire = env.EXPIRE_TIME
    scheme = env.CRYPTO_SCHEME
