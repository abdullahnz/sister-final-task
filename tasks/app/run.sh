#!/bin/sh

celery -A tasks worker -P threads --loglevel=INFO