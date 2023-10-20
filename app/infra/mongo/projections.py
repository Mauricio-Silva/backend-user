
USER_MODEL_OUT_PROJECTION = {"password": 0, "videos": 0, "friends": 0}

LOGIN_MODEL_OUT_PROJECTION = {"videos": 0, "friends": 0}

FRIENDS_PROJECTION = {"friends": 1}

VIDEOS_PROJECTION = {"_id": 0, "videos": 1}

PHOTO_PROJECTION = {"_id": 0, "photo": 1}

PASSWORD_PROJECTION = {"_id": 0, "password": 1}

PROFILE_MODEL_OUT_PROJECTION = {
    "create_at": 0,
    "update_at": 0,
    "verified_at": 0,
    "is_enabled": 0,
    "password": 0
}
