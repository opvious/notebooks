#!/usr/bin/env bash

set -o nounset
set -o errexit
set -o pipefail
shopt -s nullglob

__dirname="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

main() {
  cd "$__dirname/.."
  if [ -d venv ]; then
    . venv/bin/activate
  fi
  for p in resources/**/*.ipynb; do
    echo "Validating $p..."
    python -m opvious register-notebook -ed "$p"
  done
}

main "$@"
