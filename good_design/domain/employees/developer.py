from datetime import datetime
from random import choice

from _decimal import Decimal
from dataclasses import dataclass, field
from functools import wraps
from typing import Callable

from domain.employees.abstract import Employee
from domain.enums import ProgrammingLanguage, TaskStatus
from domain.task import Task


@dataclass
class Developer(Employee):
    """
    This class represents a developer
    """

    # init
    programming_languages: list[ProgrammingLanguage]

    # set
    tasks: list[Task] = field(default_factory=list)

    def __hash__(self) -> int:
        return id(self)

    @staticmethod
    def _validate_task_inv(method: Callable) -> Callable:
        """
        This method validates if the developer can work on the task based on the programming language required by the task

        :param method: Method to validate
        :return: Wrapper
        """
        @wraps(method)
        def wrapper(self, task: Task) -> None:
            if task.programming_language not in self.programming_languages:
                raise ValueError(
                    f"Can't add task {task} because it requires {task.programming_language} programming "
                    f"language which is not learned by {self}"
                )
            return method(self, task)
        return wrapper

    @_validate_task_inv
    def add_task(self, task: Task) -> None:
        """
        This method adds a task to the developer

        :param task: Task to add
        :return: None
        """
        self.tasks.append(task)
        print(f"Task {task} has been added to developer {self}")

    @staticmethod
    def _process_task(task: Task) -> Decimal:
        """
        This method processes the task

        :param task: task to process
        :return: None
        """
        task.started_at = datetime.now()
        task.status = TaskStatus.DEV_IN_PROGRESS

        # ... some code to process the task

        task.finished_at = datetime.now()
        task.status = TaskStatus.DONE

        return Decimal(choice(range(1, 10)))

    def do(self) -> Decimal:
        """
        This method emulates the developer's work on tasks

        :return: Number of worked periods (hours, days, etc.) spent on tasks
        """

        print(f"Developer {self} is starting to work on all tasks")

        hours_spent: Decimal = Decimal(0)

        for task in self.tasks:
            print(f"{self} is starting to work on task: {task}")

            hours_spent += self._process_task(task)

            print(f"Developer {self} has finished to work on the task {task}. Elapsed time: {hours_spent}")

        print(f"Developer {self} has finished to work on all tasks")

        return hours_spent
