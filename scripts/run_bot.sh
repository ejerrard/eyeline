#!/bin/bash
set -e
cd "$(dirname "$0")"/..
source .venv/bin/activate
python -m scripts.run_bot