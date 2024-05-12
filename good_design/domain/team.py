from dataclasses import dataclass, field

from domain.employees.developer import Developer
from good_design.domain.task import Task


@dataclass
class Team:
    """
    This class represents a team of developers
    """

    # init
    name: str

    # set
    developers: list[Developer] = field(default_factory=list)
    backlog: list[Task] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

    def add_developer(self, developer: Developer) -> None:
        """
        This method adds a developer to the team

        :param developer: developer to add
        :return: None
        """
        self.developers.append(developer)
        print(f"{developer} has been added to the team {self}")

    def add_task(self, task: Task) -> None:
        """
        This method adds a task to the team

        :param task: task to add
        :return: None
        """
        self.backlog.append(task)
        print(f"Task {task} has been added to the team {self}")
