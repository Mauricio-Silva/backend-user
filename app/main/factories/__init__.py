from .user import (
    make_db_list_users,
    make_db_get_user,
    make_db_search_user,
    make_db_create_user,
    make_db_update_user,
    make_db_delete_user,
    make_db_disable_user,
    make_db_enable_user,
    make_db_personal_profile
)
from .auth import (
    make_db_auth_login,
    make_db_update_password,
    make_db_reset_password
)
from .friend import (
    make_db_list_friends,
    make_db_add_friend,
    make_db_remove_friend
)
from .video import (
    make_db_list_videos,
    make_db_list_my_videos,
    make_db_list_friends_videos,
    make_db_add_video,
    make_db_remove_video
)
from .photo import make_db_manage_photo
