# -*- coding: utf-8 -*-
"""
Copyright: Wilde Consulting
  License: Apache 2.0

VERSION INFO::

    $Repo: fastapi_apikey
  $Author: Anders Wiklund
    $Date: 2024-03-19 14:47:37
     $Rev: 1
"""

# BUILTIN modules
import asyncio
from uuid import uuid4

# Third party modules
from pydantic import BaseModel, UUID4
from fastapi import FastAPI, Depends, HTTPException

# local modules
from security import validate_authentication

# ---------------------------------------------------------

app = FastAPI(
    redoc_url=None,
    title='API-key authentication Example'
)
""" FastAPI app instantiation. """


# -----------------------------------------------------------------------------
#
class ProcessModel(BaseModel):
    """ Define OpenApi model for API process_payload responses.

    :ivar status: Response status (FAILURE|SUCCESS).
    """
    status: str


# -----------------------------------------------------------------------------
#
class ProcessResponseModel(ProcessModel):
    """ Define OpenApi model for API process_payload responses.

    :ivar id: Task ID for the current job.
    """
    id: UUID4


# ---------------------------------------------------------
#
async def _fake_processing(payload: ProcessModel) -> bool:
    """ Fake process payload.

    :param payload: POST-body data.
    """
    await asyncio.sleep(0.5)
    return payload.status == 'SUCCESS'


# ---------------------------------------------------------
#
@app.post(
    '/process', response_model=ProcessResponseModel,
    dependencies=[Depends(validate_authentication)]
)
async def process(payload: ProcessModel) -> ProcessResponseModel:
    """**Payload processing.**

    :param payload: Process POST-body data.
    """

    if await _fake_processing(payload):
        return ProcessResponseModel(status='SUCCESS', id=f'{uuid4()}')

    raise HTTPException(status_code=500, detail="Task processing failed")
