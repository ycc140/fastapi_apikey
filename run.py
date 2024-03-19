#!/usr/bin/env python
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

# Third party modules
import uvicorn

if __name__ == "__main__":
    uv_config = {'reload': True,
                 'app': 'main:app'}
    uvicorn.run(**uv_config)
