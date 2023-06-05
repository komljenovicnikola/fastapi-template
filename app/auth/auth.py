import os

import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta


class AuthHandler:
    security = HTTPBearer()
    secret = os.environ.get("SECRET")
    algorithm = os.environ.get("ALGORITHM")

    def encode_token(self, username):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=30, minutes=0),
            'iat': datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm=self.algorithm
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)
