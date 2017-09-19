# pytodoist
Lightweight Todoist python client

## Installation

Install the python distribution with `pip`.

```bash
pip install git+https://github.com/vmoret/pytodoist.git
```

## Usage

```python
from todoist import Todoist, NewTask

todos = Todoist('<Your API token>')

# print tasks
print(todos)

# add new task
todos.append(NewTask('do nothing', 'Work', labels=['home']))
```

