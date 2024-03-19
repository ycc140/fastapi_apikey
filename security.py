# -*- coding: utf-8 -*-
"""
Copyright: Wilde Consulting
  License: Apache 2.0

VERSION INFO::

    $Repo: fastapi_apikey
  $Author: Anders Wiklund
    $Date: 2024-03-19 17:28:01
     $Rev: 2
"""

# Third party modules
from dotenv import dotenv_values
from fastapi.security import APIKeyHeader
from fastapi import HTTPException, Security, status

# Constants
API_KEY_HEADER = APIKeyHeader(name="X-API-Key")
""" Using API key authentication. """
API_KEY = dotenv_values(".env")["SERVICE_API_KEY"]
""" API-key environment value. """


# ---------------------------------------------------------
#
def validate_authentication(api_key: str = Security(API_KEY_HEADER)):
    """ Validate API key authentication.

    :param api_key: Authentication credentials.
    :raise HTTPException(401): When an incorrect API key is supplied.
    """

    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
            headers={"WWW-Authenticate": "X-API-Key"}
        )
