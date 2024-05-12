from itertools import zip_longest

from _decimal import Decimal
from collections import defaultdict
from dataclasses import dataclass, field

from domain.employees.abstract import Employee
from domain.employees.developer import Developer
from domain.task import Task
from domain.team import Team
from domain.work_reporter import WorkReporter


@dataclass
class Manager(Employee):
    """
    This class represents a manager of a team of developers. There is the following relationship between entities:
    Manager -> Teams -> Developers -> Tasks
    """

    # init
    work_reporter: WorkReporter

    # set
    teams: list[Team] = field(default_factory=list)

    def __hash__(self) -> int:
        return id(self)

    def add_team(self, team: Team) -> None:
        """
        This method adds a team to the manager

        :param team: Team to add
        :return: None
        """
        self.teams.append(team)
        print(f"Team {team} has been added to the manager {self}")

    def _distribute_tasks_among_developers(self) -> None:
        print(
            f"Manager {self} is starting to distribute tasks among all teams (assigned tasks to developers)"
        )

        for team in self.teams:
            print(f"Manager {self} is starting to distribute tasks for team {team}")

            for task in team.backlog:
                for developer in team.developers:
                    # check if the developer can work on the task
                    if task.programming_language not in developer.programming_languages:
                        continue

                    developer.add_task(task)

            print(f"Manager {self} has finished distributing tasks for team {team}")

        print(f"Manager {self} has finished distributing tasks for all teams")

    def _start_sprint_for_teams(self) -> defaultdict[Developer, Decimal]:
        developers_work_reports: defaultdict[Developer, Decimal] = defaultdict(Decimal)

        for team in self.teams:
            print(f"Manager {self} is starting sprint for team {team}")

            for developer in team.developers:
                # .do() is a synchronous method just for demonstration purposes
                hours_spent: Decimal = developer.do()
                developers_work_reports[developer] += hours_spent
                print(f"Developer {developer} has worked {hours_spent} hours")

            print(f"Manager {self} has finished sprint for team {team}")

        return developers_work_reports

    def _assign_tasks_to_teams(self, tasks: list[Task]) -> None:
        """
        This method assigns tasks to teams according to the number of tasks and teams available.
        It tries to distribute tasks as fairly as possible among all the teams.

        :param tasks: list of tasks to be assigned to teams
        :return: None
        """
        if len(tasks) <= len(self.teams):
            # case 1: teams number is equal to tasks number -> each team receives one task.
            # case 2: teams number is higher than tasks number -> the number of teams that's equal to the tasks number
            # receive tasks, the rest of the teams do not receive tasks.
            for task, team in zip_longest(tasks, self.teams, fillvalue=None):
                if any((task is None, team is None)):
                    # if either task or team is None, then the loop should break,
                    # because there are no more tasks or teams
                    break

                team.add_task(task)

        else:
            # case 3: teams number is lower than tasks number -> tasks should be spread fairly among all the teams
            index = 0
            for task in tasks:
                try:
                    self.teams[index]
                except IndexError:
                    index = 0
                finally:
                    self.teams[index].add_task(task)
                    index += 1

    def report_developers_worked_hours(
        self, developers_work_reports: defaultdict[Developer, Decimal]
    ) -> None:
        print(f"Manager {self} is starting to report developers worked hours")

        for developer, worked_periods in developers_work_reports.items():
            self.work_reporter.add_employee_work_report(
                developer, worked_periods
            )

        print(f"Manager {self} has finished reporting developers worked hours")

    def do(self, tasks: list[Task]) -> None:
        print(f"Manager {self} is starting to work")

        # assign tasks to teams (fill the backlog of each team with tasks)
        self._assign_tasks_to_teams(tasks)

        # distribute tasks among developers in teams
        self._distribute_tasks_among_developers()

        # start sprint for each team
        developers_work_reports: defaultdict[Developer, Decimal] = (
            self._start_sprint_for_teams()
        )

        # report worked periods for each developer
        self.report_developers_worked_hours(developers_work_reports)

        # report worked periods for itself
        self.work_reporter.add_employee_work_report(self, Decimal(5))

        print(f"Manager {self} has finished to work")
