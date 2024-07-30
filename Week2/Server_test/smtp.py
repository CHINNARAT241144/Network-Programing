import smtplib

message = """From: From Joe <joe@low.com>
To: To dewinet <dew>
MIME-Version: 1.0
Content-type: text/html
Subject: Test HTML Email

This is a test HTML Message sent as HTML.

<b>This is a test HTML Message.</b>
<h1>This is headling 1</h1>
"""

try:
    smtp = smtplib.SMTP("192.168.127.134")
    smtp.sendmail("dew", "dew", message)
    print("Email sent successfully")
except Exception as err:
    print(str(err))