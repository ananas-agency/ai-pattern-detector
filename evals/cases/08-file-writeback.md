---
title: Getting started with the export tool
tags: [docs, export]
---

# Getting Started With The Export Tool

In today's fast-paced world, data teams need a seamless way to move information — and that's exactly where our export tool comes in. It's not just a utility; it's a game-changer for your workflow.

To begin, install the package and run the `export --init` command. This will leverage your existing configuration and create a robust starting point.

```bash
# leverage the default profile — no flags needed
export --init --profile default
```

Once initialized, you can delve into the settings file at `config/export.yaml`, which serves as the single source of truth for every job. For the full list of options, see the [configuration reference](https://example.com/docs/export/config-reference).

```yaml
# Paths below are relative — leverage env vars for anything absolute
output_dir: ./exports
format: csv
```

Ultimately, by leveraging these powerful features, you can unlock the full potential of your data pipeline.
