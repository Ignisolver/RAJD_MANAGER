from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    OK = "OK"  # Dodany do grupy (ręcznie)
    S_C_S = "SAV"  # Potwierdzenie zapisania wysłane (API)
    ZAL_Z = "ZAL"  # Zaliczka zapłacona (ręcznie)
    R_C_S = "REG"  # Potwierdzenie zgłoszenia wysłane (API)
    NEW = ""  # Zgłoszony (google)


@dataclass
class Person:
    id_: int
    mail: str
    status: Status
    name: str
    fb: str
    surname: str
