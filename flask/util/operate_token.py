import jwt
from datetime import datetime, timedelta


# Operate Token
class OperateToken:

    def __init__(self):
        self._private_key = "zltool#123"
        pass

    # Create token
    def create_token(self, user_id, user_name, expiry_seconds):
        # Calculate expiry time
        expiry_time = datetime.utcnow() + timedelta(seconds=expiry_seconds)

        payload = {
            'exp': expiry_time,
            'user_id': user_id,
            'user_name': user_name
        }

        # Encode the key
        encode_jwt = jwt.encode(payload, self._private_key, algorithm='HS256')
        return encode_jwt

    # Decode token
    def decode_token(self, token):
        decode_jwt = -1
        # Decode the token
        try:
            decode_jwt = jwt.decode(token, self._private_key, algorithms=['HS256'])
        except jwt.PyJWTError:
            print("Token is error!")
        return decode_jwt


# Single instance
operate_token = OperateToken()
