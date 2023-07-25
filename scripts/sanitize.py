#!/usr/bin/env python3
# encoding: utf-8

"""Make notebooks JupyterLite-friendly"""

import json
import pathlib

def _clear_pip_output(data):
    for cell in _code_cells(data):
        if "%pip" in _string_value(cell["source"]):
            cell["outputs"] = []

def _code_cells(data):
    for cell in data["cells"]:
        if cell["cell_type"] == "code":
            yield cell

def _renumber_execution_counts(data):
    for i, cell in enumerate(_code_cells(data), 1):
        cell["execution_count"] = i

def _string_value(val):
    return "".join(val) if isinstance(val, list) else val

def _sanitize_markdown_output(data):
    for cell in _code_cells(data):
        for output in cell.get("outputs", []):
            for key, val in output.get("data", {}).items():
                output["data"][key] = _string_value(val)
            text = output.get("text")
            if text:
                output["text"] = _string_value(text)

_root = pathlib.Path(__file__).parent.parent.resolve()

def main():
    for p in _root.joinpath("resources").glob("**/*.ipynb"):
        print(f"Sanitizing {p}...")
        data = json.loads(p.read_text())
        _clear_pip_output(data)
        _sanitize_markdown_output(data)
        _renumber_execution_counts(data)
        p.write_text(json.dumps(data, indent=2))

if __name__ == '__main__':
    main()
