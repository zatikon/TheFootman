#!/bin/bash

set -eu

cd "$(dirname "$0")"

source venv/bin/activate

read -sp "Provide the token: "

python bot.py <(echo "$REPLY")
