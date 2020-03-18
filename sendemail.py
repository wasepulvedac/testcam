from smtplib import SMTP as Client


hostname="localhost"
port=8025

client = Client(hostname,port)
r = client.sendmail('a@example.com', ['b@example.com'], """\
From: Anne Person <anne@example.com>
To: Bart Person <bart@example.com>
Subject: A test
Message-ID: <ant>
...
Hi Bart, this is Anne.
""")