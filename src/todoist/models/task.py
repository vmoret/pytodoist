import datetime

from ..proxy import TodoistAPI
from ..immutable import Map, List
from .project import Projects
from .label import Labels


class Task(Map):
    """Represents a `Task`"""

    def __eq__(self, other):
        if isinstance(other, str):
            return self['content'] == other
        return super().__eq__(other)


class NewTask(Task):
    """Represents a new `Task`"""

    def __init__(self, content, project=None, due=None, labels=None, lang=None):

        # confirm `content` is a valid string
        if not isinstance(content, str):
            raise TypeError('NewTask(): Expected `content` to be a string')

        # initialize DTO object
        dto = dict(content=content)

        # find matching project IDs
        if project is not None:
            if not isinstance(project, str):
                raise TypeError('NewTask(): Expected `project` to be a string')
            project_ids = [x['id'] for x in Projects() if x == project]
            if len(project_ids) == 0:
                raise ValueError(
                    'NewTask(): project "{:}" was not found'.format(project)
                )
            dto.update(dict(project_id=project_ids[0]))

        # find label IDs
        if labels is not None:
            label_ids = [x['id'] for x in Labels() if x in labels]
            dto.update(label_ids=label_ids)

        # convert `due` value to `due_*` keys
        if due is not None:
            if isinstance(due, str):
                dto.update(dict(due_string=due))
                if lang is not None:
                    dto.update(dict(due_lang=lang))
            elif isinstance(due, datetime.date):
                dto.update(dict(due_date=due.isoformat()))
            elif isinstance(due, datetime.datetime):
                dto.update(dict(due_datetime=due.isoformat()))
            else:
                raise TypeError('NewTask(): unsupported type for `due`')
        else:
            dto.update(dict(due_string='Today'))

        super().__init__(dto)


class Tasks(List):
    """Represents a `Task` list"""

    def __init__(self, url='tasks', **kwargs):
        super().__init__([Task(x) for x in TodoistAPI().get(url, **kwargs)])

    def append(self, task):
        if not isinstance(task, NewTask):
            raise TypeError('Tasks.append(): Expected `task` to be a NewTask')
        dto = TodoistAPI().post('tasks', task)
        return self.data.append(Task(dto))

    def __delitem__(self, key):
        ix = self.data[key]['id']
        TodoistAPI().delete('tasks/{:}'.format(ix))
        return self.data.__delitem__(key)

