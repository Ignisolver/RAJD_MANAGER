from typing import List

from utils import Status, Person


class Persons:
    def __init__(self, persons: List[Person]):
        self.persons = persons

    def _get_persons(self, filter_):
        persons = list(filter(filter_, self.persons))
        return Persons(persons)

    def get_persons_to_send_registration_confirm(self):
        register_filter = lambda x: x.status == Status.NEW.value
        return self._get_persons(register_filter)

    def get_persons_to_send_sign_up_confirm(self):
        sign_up_filter = lambda x: x.status == Status.ZAL_Z.value
        return self._get_persons(sign_up_filter)

    def get_persons_who_must_pay(self):
        pay_filter = lambda x: x.status == Status.R_C_S.value
        return self._get_persons(pay_filter)

    def get_persons_who_wait_to_fb(self):
        fb_filter = lambda x: x.status == Status.S_C_S.value
        return self._get_persons(fb_filter)

    def get_statuses(self):
        return [[p.status] for p in self.persons]

    def update_status(self, persons, status):
        for p in persons:
            id_ = self.get_list_id(p)
            self.persons[id_].status = status.value

    @staticmethod
    def get_list_id(person: Person):
        return person.id_ - 1

    def __repr__(self):
        txt = ""
        for p in self.persons:
            txt += str(p) + "\n"
        return txt

    def __len__(self):
        return len(self.persons)

    def __iter__(self):
        return iter(self.persons)
