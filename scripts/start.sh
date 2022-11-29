#!/bin/sh
source .venv/bin/activate
pip install -r requirements.txt
if ! [ pip freeze | grep pylint ]
then
    pip install pylint
fi
#pylint --generate-rcfile > .pylintrc
docker network create my-network
~/repos/CI_CD_DevOps_final/scripts/db.sh
~/repos/CI_CD_DevOps_final/scripts/flask.sh
