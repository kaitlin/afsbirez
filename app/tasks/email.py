# -*- coding: utf-8 -*-
"""
    tasks.email
    ~~~~~~~~~~~

    :author: 18F
    :copyright: © 2014-2015, 18F
    :license: CC0 Public Domain License, see LICENSE for more details.
"""
from flask.ext.mail import Message

from . import workq
from ..framework.extensions import mail, security

@workq.task
def send_email(message):
    mail.send(msg)

def send_message(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    send_email.delay(msg)

@workq.task
def add(x, y):
    """docstring for add"""
    return x+y
