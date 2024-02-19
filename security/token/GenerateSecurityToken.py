"""
    Used to generate a security token using pyjwt.
"""
from datetime import timedelta

import jwt


def __generate_token__(payload: dict, secret: str, algorithm: str, expiry: int):
    return jwt.encode(payload, secret, algorithm=algorithm, expires_delta=timedelta(seconds=expiry))


class GenerateSecurityToken:
    """
    Generates a security token using pyjwt.
    @:param payload: The payload to be used for generating the token.
    @:param secret: The secret to be used for generating the token.
    @:param algorithm: The algorithm to be used for generating the token.
    @:param expiry: The expiry to be used for generating the token. the time is in seconds.
    """

    def __init__(self, payload: dict, secret: str, algorithm: str, expiry: int):
        self.payload = payload
        self.secret = secret
        self.algorithm = algorithm
        self.expiry = expiry

    """
    Generates the token.
    """

    def generate(self):
        return __generate_token__(self.payload, self.secret, self.algorithm, self.expiry)
