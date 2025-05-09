# Resources Directory

This directory contains static resources for the Iterative Prisoner's Dilemma project.

## Contents

- Images for documentation
- Data files for simulations
- Other static assets

## Usage

Resources can be loaded in Python code using:

```python
import os

def get_resource_path(filename):
    """Get the absolute path to a resource file."""
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__), 
        '..', 'res', filename
    ))
```
