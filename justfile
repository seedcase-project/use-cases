@_default:
    just --list --unsorted

# Run all the build recipes
run-all: install-deps format-python check-python check-commits

# Install Python package dependencies
install-deps:
  poetry install

# Check Python code with the linter for any errors that need manual attention
check-python:
  poetry run ruff check .

# Reformat Python code to match coding style and general structure
format-python:
  poetry run ruff check --fix .
  poetry run ruff format .

# Run checks on commits with non-main branches
check-commits:
  #!/bin/zsh
  if [[ $(git rev-parse --abbrev-ref HEAD) != "main" ]]
  then
    poetry run cz check --rev-range main..HEAD
  fi
