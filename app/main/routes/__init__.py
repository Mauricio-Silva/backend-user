from .user import router as user_router
from .auth import router as auth_router
from .friend import router as friend_router
from .video import router as video_router
from .admin import router as admin_router


ROUTES = (
    admin_router,
    auth_router,
    user_router,
    friend_router,
    video_router
)
