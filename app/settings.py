# -*- coding: utf-8 -*-
"""
    sbirez.settings
    ~~~~~~~~~~~~~~~

    :author: 18F
    :copyright: © 2014-2015, 18F
    :license: CC0 Public Domain License, see LICENSE for more details.
"""

# Flask
DEBUG = True
TESTING = False
SECRET_KEY = 'super secret key - override with instance configuration'

# Framework
USE_CDN = False
USE_PJAX = False

# Flask-DebugToolbar
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Database / Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/sbirez.db"

# Flask-Mail
# Add your mail configuration to the instance configuration template
# generated by ansible in playbooks/templates/setting.cfg
# Keep any 'secret' passwords in ansible-vault protected files, e.g.
# playbooks/vars/secrets.yml
# By default, all emails from Flask-Security have been disabled.

# Flask-Security basics
SECURITY_CHANGEABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = False
SECURITY_REGISTERABLE = True
SECURITY_TRACKABLE = True

# Flask-Security redirects
SECURITY_POST_CHANGE_VIEW = None
SECURITY_POST_CONFIRM_VIEW = '/'
SECURITY_POST_LOGIN_VIEW = '/'
SECURITY_POST_LOGOUT_VIEW = '/'
SECURITY_POST_REGISTER_VIEW = '/'
SECURITY_POST_RESET_VIEW = None

# Flask-Security options
SECURITY_FLASH_MESSAGES = True
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'another super secret key'

# NOTE: We are supplying our own password context from passlib; no additional
# password salts are requried. We have to override the default of
# Flask-Security in order to make this happen.
#
# You can generate random salts for the remaining Flask-Security salts by using
# the scripts/generate_salts script in the playbooks directory.  This will
# generate a new vars/salts.yml file. You should protect that file using
# ansible-vault.

# Flask-Security email options
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False
SECURITY_SEND_REGISTER_EMAIL = False

# Celery
CELERY_BROKER_URL='redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND='redis://127.0.0.1:6379'
CELERYD_PREFETCH_MULTIPLIER=0
CELERY_IMPORT = [
    'sbirez.tasks',
]
CELERY_INCLUDE = [
    'sbirez.tasks',
]
CELERYBEAT_SCHEDULE = {
#   example of a celery beat entry
#   'database-maintenence': {
#       'task': 'sbirez.tasks.database.maintenence',
#       'schedule': crontab(minute=0, hour=4, day_of_month='*/3')
#   }
}

