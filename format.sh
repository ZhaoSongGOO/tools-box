#!/usr/bin/env bash

find . -type f -name "*.py" -not -path "./.venv/*"| grep '\.py$' | xargs black


