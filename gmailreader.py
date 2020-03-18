import imaplib
import credentials

imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
'''
credentials.email ='wascuevas@gmail.com'
credentials.passwd='1q2w3e4rp0t0n1nj4'
'''


username = 'wascuevas@gmail.com'
password = 'p0t0p0t0r1c0r1c0'
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

server.login(username, password)
server.select('INBOX')

data = server.uid('search',None, '(SUBJECT "MY QUERY HERE!")')
print(data)