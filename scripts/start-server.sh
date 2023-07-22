#!/usr/bin/env bash

# Convenience script to start a Jupyter notebook server in a self-contained
# virtualenv.

set -o nounset
set -o errexit
set -o pipefail
shopt -s nullglob

__dirname="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

main() {
  cd "$__dirname/.."
  if [ -d venv ]; then
    . venv/bin/activate
  else
    python3 -m venv venv
    . venv/bin/activate
  fi
  pip install jupyter
  pip install -r requirements.txt
  jupyter notebook resources
}

main "$@"
