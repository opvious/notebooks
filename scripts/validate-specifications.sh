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
  for p in notebooks/*.ipynb; do
    echo "Validating $p..."
    python -m opvious register-notebook -d "$p"
  done
  for p in sources/*.md; do
    echo "Validating $p..."
    python -m opvious register-sources -d "$p"
  done
}

main "$@"
