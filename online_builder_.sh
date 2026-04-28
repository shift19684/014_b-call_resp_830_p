#!/bin/sh

echo "online builder turned"

python3 -m venv ./.bask/.myenv
source ./.bask/.myenv/bin/activate
pip install --upgrade pip
pip install awsiotsdk==1.27.0 awscrt==0.30.0
pip install -U pyarmor
deactivate
