#!/usr/bin/env bash
# exit on error
set -o errexit

# Install uv
pip install uv

# Sync dependencies using uv (uses pyproject.toml)
uv sync --frozen