#!/bin/bash

uvicorn app.main:app --host 0.0.0.0 --port 5000 --timeout-keep-alive 0 --workers 3