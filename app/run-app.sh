#!/bin/bash

uvicorn app.main:app --host 0.0.0.0 --port 80 --timeout-keep-alive 10