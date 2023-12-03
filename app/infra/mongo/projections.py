
USER_MODEL_OUT_PROJECTION = {"password": 0, "videos": 0, "friends": 0}

LOGIN_MODEL_OUT_PROJECTION = {"videos": 0, "friends": 0}

FRIENDS_PROJECTION = {"friends": 1}

VIDEOS_PROJECTION = {"_id": 0, "videos": 1}

PASSWORD_PROJECTION = {"_id": 0, "password": 1}

DISABLE_ACCOUNTS = {"is_enabled": 1, "create_at": 1}

ADMIN_PROJECTION = {
    "name": 1,
    "username": 1,
    "email": 1
}

PROFILE_MODEL_OUT_PROJECTION = {
    "create_at": 0,
    "update_at": 0,
    "verified_at": 0,
    "is_enabled": 0,
    "password": 0
}
