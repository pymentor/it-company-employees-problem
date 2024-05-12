from typing import Any

from _decimal import Decimal
from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.enums import Role, Employment


@dataclass
class Employee(ABC):
    """
    This class represents an employee - base class for all company employees
    """

    # init
    name: str
    email: str
    role: Role
    employment: Employment
    payment_rate: Decimal

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def do(self, *args, **kwargs) -> Any:
        """
        Fabric method to be implemented in subclasses as a public method, that performs the employee's work
        """
        pass
