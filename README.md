# pytodoist
Lightweight Todoist python client

## Installation

Install the python distribution with `pip`.

```bash
pip install git+https://github.com/vmoret/pytodoist.git
```

## Usage

```python
from todoist import Todoist

todos = Todoist('<Your API token>')

print(todos)

todos.append('do nothing', 'Work', 'tomorrow')
```
