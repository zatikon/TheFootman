#!/bin/bash

set -eu

cd "$(dirname "$0")"

source venv/bin/activate

python -m pip freeze | tee requirements.txt
