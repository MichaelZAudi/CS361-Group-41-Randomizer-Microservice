#!/usr/bin/env bash
# start server using gunicorn
gunicorn stats_app:app --bind 0.0.0.0:$PORT