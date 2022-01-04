#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Script send an email using MS Exchange server to a defined address list.
# There are 8 system environments needed for this script.

import os
import time
from sys import argv
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, Configuration
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter

BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

'''
POSTSERVER = str(os.environ.get("POST_SERVER"))
POSTDOMAIN = str(os.environ.get("POST_DOMAIN"))
POSTUSERNAME = str(os.environ.get("POST_USERNAME"))
POSTPASSWORD = str(os.environ.get("POST_PASSWORD"))
POSTFROMADDRESS = str(os.environ.get("POST_FROM_ADDRESS"))
POSTTOADDRESS = str(os.environ.get("POST_TO_ADDRESS_LIST"))
POSTSUBJECT = str(os.environ.get("POST_SUBJECT"))
POSTMESSAGE = str(os.environ.get("POST_MESSAGE"))
'''

def app_email_sender(receiver_address: str, subject: str, mail_content: str) -> None:
    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
    credentials = Credentials(
        username=POSTDOMAIN + "\\" + POSTUSERNAME, password=POSTPASSWORD
    )
    config = Configuration(server=POSTSERVER, credentials=credentials)

    a = Account(
        primary_smtp_address=POSTFROMADDRESS,
        autodiscover=False,
        config=config,
        access_type=DELEGATE,
    )

    m = Message(
        account=a,
        subject=subject,
        body=mail_content,
        to_recipients=[Mailbox(email_address=receiver_address)],
    )
    m.send_and_save()
    print("E-mail have been sent to {}".format(POSTTOADDRESS))


if __name__ == "__main__":
    receiver_addresses = list(POSTTOADDRESS.split(","))
    for receiver_address in receiver_addresses:
        app_email_sender(receiver_address, POSTSUBJECT, POSTMESSAGE)
