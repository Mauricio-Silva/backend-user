<!-- cSpell:disable -->
# SnapCut

Instituto  Federal de Educação, Ciência e Tecnologia de Mato Grosso do Sul - [IFMS](https://www.ifms.edu.br/campi/campus-tres-lagoas)<br/>
Tecnologia em Análise e Desenvolvimento de Sistemas - TADS6<br/>
Unidade Curricular: Eletiva

## Team

- [Luiz Gustavo](https://github.com/Guuhp): Email Service
- [Mauricio da Silva](https://github.com/Mauricio-Silva): Backend-User
- [Rangel](https://github.com/rangel3l2): Frontend

## Environment

### MongoDB

To specify the MongoDB URI, you can define **MONGODB_URI** in the [Atlas MongoDB Cloud](https://www.mongodb.com/atlas/database) format:

> mongodb+srv//user:```<password>```@cluster.domain

Or define in the [Docker](https://hub.docker.com/_/mongo) format, specially for the [6-jammy](https://hub.docker.com/layers/library/mongo/6-jammy/images/sha256-0a50c7d53df2f2a6b17a9636ab3db737a98457cfba8abf87da3d4e62cb475a07?context=repo&tab=vulnerabilities) tag we are using:

> mongodb://localhost:```<port>```

You can set **PASSWORD** depending on whether the MongoDB connection you are using needs authentication or not.

### Email Service

This application uses an external email service that must be configured by setting **EMAIL_SERVICE_BASE_URL** and **EMAIL_SERVICE_ACCESS_TOKEN**.

### JWT Authentication

[JWT](https://jwt.io/) uses a secret private key, that you must specify by setting **SECRET_KEY**, and an algorithm (**ALGORITHM**, default is **HS256**) for signing the claims to encode, validate, and decode the JWT token.

For administration purposes and to make changes to other users of the application, you can rule as a superuser using a personal **ACCESS_KEY** that must be set.

You can also specify a **CRYPTO_SCHEME** to be used to hash and verify the passwords (default is **bcrypt**), and the expiration time of the JWT token by setting **EXPIRE_ACCESS_TOKEN_TIME** (default is **480** minutes or **8** hours).

Accounts must be verified within the time defined in **EXPIRE_CHECK_ACCOUNT_TIME** (default is **20** minutes), while passwords must be reset within the time defined in **EXPIRE_RESET_PASSWORD_TIME** (default is **10** minutes).

```bash
# Generate a random secret key for JWT signing
$  openssl rand -hex 32
```

## Run

### Docker

```bash
# Start the MongoDB Docker Compose
$ docker compose up -d
```

### Makefile

```bash
# Run application locally
$ make dev-run
$ make dev-reload

# Run application with host and port
$ make prod-run
$ make prod-reload
```
