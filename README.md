# Optimization examples

## Model sources

This repository features [specifications](/sources) for optimization models
spanning a variety of domains. For example, it includes formulations to:

+ [Select portfolio stocks](/sources/portfolio-selection.md)
+ [Allocate retail products](/sources/product-allocation.md)
+ [Pick the best Fantasy Premier League team](/sources/fantasy-premier-league.md)

## Python notebooks

This repository also contains [notebooks](/notebooks) which show how to
integrate data from various sources. You can try them out via the following
command:

```sh
./scripts/start-notebook-server.sh
```

This will start a [Jupyter][] notebook server in a virtualenv with all required
dependencies. This command requires a valid [Opvious API token][token] set as
`$OPVIOUS_TOKEN` environment variable.

[Jupyter]: https://jupyter.org/
[token]: https://hub.beta.opvious.io/authorizations
