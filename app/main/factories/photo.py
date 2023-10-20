from app.data.usecases.photo import DbManagePhoto
from app.infra.mongo import PhotoMongoRepository


def make_db_manage_photo() -> DbManagePhoto:
    photo_mongo_repository = PhotoMongoRepository()
    return DbManagePhoto(photo_mongo_repository)
