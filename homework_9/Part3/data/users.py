import dataclasses
import enum
import datetime
from typing import Optional

class Gender(enum.Enum):
    MALE = 'Male'
    FEMALE = 'Female'

class Hobbies(enum.Enum):
    SPORTS = 'Sports'
    MUSIC = 'Music'
    READING = 'Reading'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    gender: Gender
    date_of_birth: datetime.date
    avatar: Optional[str] = None
    subjects: Optional[str] = None
    hobbies: Optional[Hobbies] = None
    current_address: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None

    def formatted_year(self) -> str:
        """Возвращает год как строку."""
        return str(self.date_of_birth.year)

    def formatted_month(self) -> str:
        """Возвращает месяц в текстовом формате."""
        return self.date_of_birth.strftime("%B")

    def formatted_day(self) -> str:
        """Возвращает день месяца с ведущим нулем."""
        return f"{self.date_of_birth.day:02d}"
   