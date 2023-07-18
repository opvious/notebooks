#!/usr/bin/env bash

set -o nounset
set -o errexit
set -o pipefail
shopt -s nullglob

main() {
  if [ -d venv ]; then
    . venv/bin/activate
  fi
  for p in notebooks; do
    python -m opvious register-notebook -d "$p"
  done
  for p in sources; do
    python -m opvious register-sources -d "$p"
  done
}

main "$@"
