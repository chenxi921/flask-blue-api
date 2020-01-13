#!/usr/bin/env bash

port=${1:-8999}
NUM_WORKERS=${2:-4}
env=${3:-dev}

export ENV=${env}

PROJ_ROOT=$(dirname $0)
if [ -d ${PROJ_ROOT} ]; then
  source "`pipenv --venv`/bin/activate"
fi


exec gunicorn manager:app \
  -b 0.0.0.0:${port} \
  -w ${NUM_WORKERS}
  --env ${env}