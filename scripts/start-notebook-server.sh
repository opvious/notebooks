#!/usr/bin/env bash

set -o nounset
set -o errexit
set -o pipefail
shopt -s nullglob

main() {
  if ! [ -d venv ]; then
    python3 -m venv venv
  fi
  . venv/bin/activate
  pip install jupyter opvious pandas yfinance
  jupyter notebook notebooks
}

main "$@"
