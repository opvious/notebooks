# Optimization examples

## Python notebooks

This repository features various [notebooks](/notebooks) which show how to solve
optimization problems with Opvious. They showcase how to use the [Python SDK][]
and integrate with various data sources. Most can be run directly from your
browser, for example:

+ [Bin packing](https://www.opvious.io/examples/lab?path=bin-packing.ipynb)
+ [Product allocation](https://www.opvious.io/examples/lab?path=product-allocation.ipynb)
+ [Sudoku](https://www.opvious.io/examples/lab?path=sudoku.ipynb)

Each notebook can also be run locally. This repo contains a convenience script
to start a [Jupyter][] notebook server in a virtualenv with all required
dependencies:

```sh
./scripts/start-notebook-server.sh
```


## Model sources

This repository also contains [specifications](/sources) for optimization models
spanning a variety of domains. For example, it includes formulations to:

+ [Select portfolio stocks](/sources/portfolio-selection.md)
+ [Allocate retail products](/sources/product-allocation.md)
+ [Pick the best Fantasy Premier League team](/sources/fantasy-premier-league.md)


[Python SDK]: https://opvious.readthedocs.io/
[Jupyter]: https://jupyter.org/
[token]: https://hub.beta.opvious.io/authorizations
