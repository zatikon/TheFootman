#!/bin/bash

set -eu

cd "$(dirname "$0")"

[[ -d venv ]] || python3 -m venv venv

source venv/bin/activate

python -m pip install -r requirements.txt
