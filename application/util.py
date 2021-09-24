from application import app
from hashlib import sha256

def hashpw(password: str) -> str:
    return sha256((password+app.config['SECRET_KEY'])\
            .encode()).hexdigest()
