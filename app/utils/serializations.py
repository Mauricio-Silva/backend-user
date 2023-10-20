from bson import ObjectId
from datetime import datetime


def serialize_object_id(field: ObjectId) -> str:
    return str(field)


def serialize_datetime(field: datetime) -> str:
    return field.strftime("%d-%m-%Y %H:%M:%S")


def serialize_list(field: list) -> int:
    return 0 if field is None else len(field)
