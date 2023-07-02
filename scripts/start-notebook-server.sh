#!/usr/bin/env bash

# Convenience script to start a Jupyter notebook server in a self-contained
# virtualenv.

set -o nounset
set -o errexit
set -o pipefail
shopt -s nullglob

fail() { # [MSG]
  if (($# > 0)); then
    echo "error: $1" >&2
  fi
  exit 2
}

main() {
  if [ -d venv ]; then
    . venv/bin/activate
  else
    python3 -m venv venv
    . venv/bin/activate
  fi
  pip install jupyter 'opvious>=0.16.0' pandas yfinance
  jupyter notebook notebooks
}

main "$@"
