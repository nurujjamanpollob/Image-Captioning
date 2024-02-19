"""
    This class is used to verify the security token. It usages pyjwt to verify the token.

"""
import jwt
from datetime import datetime
from datetime import timedelta


class VerifySecurityToken:
    """
    Used to verify the security token. It usages pyjwt to verify the token.
    @:param token: The token to be verified.
    @:param secret: The secret to be used for verifying the token.
    @:param algorithm: The algorithm to be used for verifying the token.
    """

    def __init__(self, token: str, secret: str, algorithm: str):
        self.token = token
        self.secret = secret
        self.algorithm = algorithm

    """
    Verifies the token.
    """

    def verify(self):
        return jwt.decode(self.token, self.secret, algorithms=[self.algorithm])

    """
    Verifies the token and checks if it is expired.
    """

    def verify_and_check_expiry(self):
        decoded = jwt.decode(self.token, self.secret, algorithms=[self.algorithm])
        expiry = datetime.fromtimestamp(decoded['exp'])
        if datetime.now() > expiry:
            return False
        return True

    """
    Verifies the token and checks if it is expired. It also returns the decoded token.
    """

    def verify_and_check_expiry_with_decoded(self):
        decoded = jwt.decode(self.token, self.secret, algorithms=[self.algorithm])
        expiry = datetime.fromtimestamp(decoded['exp'])
        if datetime.now() > expiry:
            return False, decoded
        return True, decoded

    """Verifies the token and checks if it is expired. It also returns the decoded token. It also returns the time 
    left for the token to expire."""

    def verify_and_check_expiry_with_decoded_and_time_left(self):
        decoded = jwt.decode(self.token, self.secret, algorithms=[self.algorithm])
        expiry = datetime.fromtimestamp(decoded['exp'])
        if datetime.now() > expiry:
            return False, decoded, timedelta(0)
        return True, decoded, expiry - datetime.now()
