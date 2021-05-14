from json import load
from datetime import datetime
from passlib.context import CryptContext
from config import DATASET_FILE_PATH

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)


def encrypt_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def get_workout_data():
    with open(DATASET_FILE_PATH, "r") as read_file:
        data = load(read_file)
        return data


def get_timestamp():
    timestamp = datetime.now()
    created_on = timestamp.isoformat()
    return created_on
