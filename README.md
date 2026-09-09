# genpark-cocke-younger-kasami-cyk-pcfg-parser-skill

[![GitHub stars](https://img.shields.io/github/stars/Alpha-Park/genpark-cocke-younger-kasami-cyk-pcfg-parser-skill?style=social)](https://github.com/Alpha-Park/genpark-cocke-younger-kasami-cyk-pcfg-parser-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent CYK (Cocke-Younger-Kasami) Probabilistic Context-Free Grammar (PCFG) Parser

Part of the **GenPark Autonomous Natural Language Processing & Automata Theory Architecture**.

## Architecture Overview

```mermaid
graph TD
    A[Tokenized Sentence Sequence] --> B[Chomsky Normal Form PCFG Rules]
    B --> C[Diagonal Terminal Inferences Layer 1]
    C --> D[Dynamic Programming Triangular Table Bottom-Up]
    D --> E[Binary Subtree Branch Span Combinations]
    E --> F[Viterbi Most Probable Subtree Extraction]
    F --> G[Root Start Symbol S Syntactic Parse Tree]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies.
- **Production-Grade Design**: Type annotations, robust chart parsing, multi-pattern matching.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/Alpha-Park/genpark-cocke-younger-kasami-cyk-pcfg-parser-skill.git
cd genpark-cocke-younger-kasami-cyk-pcfg-parser-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
