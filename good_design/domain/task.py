from dataclasses import dataclass
from datetime import datetime

from good_design.domain.enums import ProgrammingLanguage, TaskStatus


@dataclass
class Task:
    """
    This class represents a task for a developer task
    """

    # init
    name: str
    description: str
    started_at: datetime | None
    finished_at: datetime | None
    programming_language: ProgrammingLanguage
    status: TaskStatus = TaskStatus.NEW

    def __str__(self) -> str:
        return self.name
