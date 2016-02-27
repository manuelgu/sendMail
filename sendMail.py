#!/usr/bin/python

import smtplib
import traceback
import sys

# Check if an argument via ./sendMail.py "The Argument" is provided
if len(sys.argv) > 1:
   firstArg = str(sys.argv[1])
else:
   sys.exit('Usage: ./sendMail.py "Your Text"')

# Global variables
sender = 'sender@email.com'
key = 'password'
receivers = ['your@receiver.com']

message = """From: You <sender@email.com>
To: Somebody <your@receiver.com>
Subject: The Very Cool E-Mail

{0}
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.login(sender, key)
   smtpObj.sendmail(sender, receivers, message.format(firstArg))         
   print "Successfully sent email"
except:
   print "Error: Unable to send email"
   print traceback.format_exc()
smtpObj.quit()
