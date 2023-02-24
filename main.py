from messages_maker import create_registration_msg, create_sign_up_msg, \
    create_sum_up_message
from my_gmail import MyGmail
from my_sheet import MySheet
from refresh_token import refresh_token
from utils import Status


def manage_new_persons(persons, gmail):
    new_reg = persons.get_persons_to_send_registration_confirm()
    for person in new_reg:
        message = create_registration_msg(person)
        gmail.send_message(message)
    persons.update_status(new_reg, Status.R_C_S)
    return new_reg


def manage_payed(persons, gmail):
    payed = persons.get_persons_to_send_sign_up_confirm()
    for person in payed:
        message = create_sign_up_msg(person)
        gmail.send_message(message)
    persons.update_status(payed, Status.S_C_S)
    return payed


def sum_up(gmail, persons, amount, new_reg, payed):
    wait_for_fb = persons.get_persons_who_wait_to_fb()
    must_pay = persons.get_persons_who_must_pay()
    message = create_sum_up_message(amount, new_reg, payed, must_pay,
                                    wait_for_fb)
    gmail.send_message(message)


def main():
    refresh_token()
    ms = MySheet()
    gmail = MyGmail()
    persons = ms.get_persons()

    amount = len(persons)

    new_reg = manage_new_persons(persons, gmail)
    payed = manage_payed(persons, gmail)
    if len(new_reg) > 0 or len(payed) > 0:
        ms.update_statuses(persons.get_statuses())
        sum_up(gmail, persons, amount, new_reg, payed)


if __name__ == '__main__':
    main()
