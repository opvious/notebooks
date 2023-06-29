#!/usr/bin/env python3
# encoding: utf-8

"""Make notebooks JupyterLite-friendly"""

import json
import pathlib

_BOUND = ">=0.14.0"

_PREAMBLE_SOURCE_FORMAT = """
import sys
if "pyodide" in sys.modules:
    import piplite
    await piplite.install('opvious{}')
"""

def _preamble_cell(bound):
    return {
        "cell_type": "code",
        "metadata": {},
        "source": _PREAMBLE_SOURCE_FORMAT.format(bound).strip(),
        "outputs": [],
        "execution_count": 0,
    }

def _ensure_preamble(data, preamble):
    cells = data["cells"]
    first = _string_value(cells[0]["source"]) if cells else ""
    if "pyodide" in first:
        cells[0] = preamble
    else:
        cells.insert(0, preamble)

def _string_value(val):
    return "".join(val) if isinstance(val, list) else val

def _sanitize_markdown_output(data):
    for cell in data["cells"]:
        if cell["cell_type"] != "code":
            continue
        for output in cell.get("outputs", []):
            for key, val in output.get("data", {}).items():
                output["data"][key] = _string_value(val)
            text = output.get("text")
            if text:
                output["text"] = _string_value(text)

_root = pathlib.Path(__file__).parent.parent.resolve()

def main():
    preamble = _preamble_cell(_BOUND)
    for p in _root.joinpath("notebooks").glob("*.ipynb"):
        print(f"Sanitizing {p}...")
        data = json.loads(p.read_text())
        _ensure_preamble(data, preamble)
        _sanitize_markdown_output(data)
        p.write_text(json.dumps(data, indent=2))

if __name__ == '__main__':
    main()
