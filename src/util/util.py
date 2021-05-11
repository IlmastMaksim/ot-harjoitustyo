from json import load
from datetime import datetime
from re import search, compile
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)


def validate_password(password):
    reg = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    compiled_reg = compile(reg)
    return search(compiled_reg, password)


def encrypt_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def get_workout_data():
    with open("./src/data/dataset.json", "r") as read_file:
        data = load(read_file)
        return data


def get_timestamp():
    timestamp = datetime.now()
    created_on = timestamp.isoformat()
    return created_on
