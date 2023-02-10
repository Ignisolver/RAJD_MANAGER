import base64
from email.message import EmailMessage

import yaml

# TODO: Update link
from config import FB_GROUP_LINK, MY_MAIL, MSG_PATH
from persons_manager import Persons
from utils import Person


def _get_content(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data


def create_registration_msg(person: Person):
    data = _get_content(
        MSG_PATH.joinpath("tekst_potwierdzenia_przyjęcia_zgłoszenia.yaml"))
    subject = data["SUB"]
    content = data["CONTENT_1"] + f" {person.name},\n" + data["CONTENT_2"]
    message = _create_message(person.mail, subject, content)
    return message


def create_sign_up_msg(person: Person):
    data = _get_content(
        MSG_PATH.joinpath("tekst_potwierdzenia_ZAPISANIA.yaml"))
    subject = data["SUB"]
    content = data["CONTENT_1"] + f" {person.name},\n" + data["CONTENT_2"]
    content = content + " " + FB_GROUP_LINK + "\n" + data["CONTENT_3"]
    message = _create_message(person.mail, subject, content)
    return message


def _format(persons: Persons):
    persons = _change_to_names_ans_surnames(persons)
    persons_str = "\n\t" + "\n\t".join(persons) + "\n"
    return persons_str


def create_sum_up_message(person_am, send_reg_confirm, send_sign_up_confirm,
                          wait_for_money, invited_to_fb):
    data = _get_content(MSG_PATH.joinpath(("potwierdzenie_mi.yaml")))
    txt = data["COUNTER"] + str(person_am) + "\n"
    txt += data["SEND_CONFIRM"] + _format(send_reg_confirm)
    txt += data["SIGN_UP"] + _format(send_sign_up_confirm)
    txt += data["MONEY"] + _format(wait_for_money)
    txt += data["INV_FB"] + _format(invited_to_fb)
    message = _create_message(MY_MAIL, "RAJD-RAPORT", txt)
    return message


def _create_message(email, subject, content: str):
    message = EmailMessage()
    message.set_content(content)
    message['To'] = email
    message['From'] = MY_MAIL
    message['Subject'] = subject
    message.set_charset("utf-8")

    message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    return message


def _change_to_names_ans_surnames(persons: Persons):
    return [f"{p.name} {p.surname}" for p in persons]
