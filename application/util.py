from hashlib import sha256

from application import app


def hashpw(password: str) -> str:
    return sha256((password+app.config['SECRET_KEY'])\
            .encode()).hexdigest()
