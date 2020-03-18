from datetime import datetime
from smtpd  import SMTPServer
from pprint import pprint
import asyncore


class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        print("process_message")
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),self.no)
        pprint(peer)
        pprint(mailfrom)
        with open(filename, 'w') as f:
            f.write(data)
            
        print('%s saved.' % filename)
        self.no += 1


def run():
    # start the smtp server on localhost:1025
    foo = EmlServer(("0.0.0.0", 1025), None)
    print("Start server")
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print("error")
        pass
    print("Start server")


if __name__ == '__main__':
    run()