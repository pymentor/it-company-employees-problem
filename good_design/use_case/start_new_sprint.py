from decimal import Decimal, getcontext

from domain.employees.accountant import Accountant
from domain.employees.manager import Manager
from domain.employees.developer import Developer
from good_design.domain.enums import (
    Role,
    Employment,
    ProgrammingLanguage,
    TaskStatus,
)
from good_design.domain.task import Task
from good_design.domain.team import Team
from good_design.domain.work_reporter import WorkReporter

getcontext().prec = 2


def start_new_sprint() -> None:
    # create work report receiver
    work_report_receiver = WorkReporter()

    # create regular accountant
    regular_accountant = Accountant(
        "Eve White",
        "eve@company.com",
        Role.ACCOUNTANT,
        Employment.REGULAR,
        Decimal(1000),
        work_report_receiver,
    )

    # create regular manager
    regular_manager = Manager(
        "Alice Brown",
        "alice@company.com",
        Role.MANAGER,
        Employment.REGULAR,
        Decimal(2000),
        work_report_receiver,
    )

    # create team 1
    team1 = Team("Team 1")

    # create regular developer 1
    regular_developer1 = Developer(
        "Bob Green",
        "bob@company.com",
        Role.DEVELOPER,
        Employment.REGULAR,
        Decimal(1500),
        [ProgrammingLanguage.PYTHON],
    )

    # create regular developer 2
    regular_developer2 = Developer(
        "Charlie White",
        "charlie@company.com",
        Role.DEVELOPER,
        Employment.REGULAR,
        Decimal(1500),
        [ProgrammingLanguage.JAVASCRIPT],
    )

    # add developers to team 1
    team1.add_developer(regular_developer1)
    team1.add_developer(regular_developer2)

    # add team 1 under the management of the regular manager
    regular_manager.add_team(team1)

    # create tasks
    task1 = Task(
        name="Task 1",
        description="Task 1 description",
        started_at=None,
        finished_at=None,
        programming_language=ProgrammingLanguage.PYTHON,
        status=TaskStatus.NEW,
    )

    task2 = Task(
        name="Task 2",
        description="Task 2 description",
        started_at=None,
        finished_at=None,
        programming_language=ProgrammingLanguage.JAVASCRIPT,
        status=TaskStatus.NEW,
    )

    task3 = Task(
        name="Task 3",
        description="Task 3 description",
        started_at=None,
        finished_at=None,
        programming_language=ProgrammingLanguage.PYTHON,
        status=TaskStatus.NEW,
    )

    # do the manager job
    regular_manager.do([task1, task2, task3])

    # do the accountant job
    regular_accountant.do()
