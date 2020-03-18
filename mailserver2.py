from   aiosmtpd.controller import Controller
import asyncio
import logging
import sys
class ExampleHandler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        print("handle_RCPT")
        '''
        if not address.endswith('@example.com'):
            return '550 not relaying to that domain'
        '''
        envelope.rcpt_tos.append(address)
        return '250 OK'
    async def handle_DATA(self, server, session, envelope):
        print('Message from %s' % envelope.mail_from)
        print('Message for %s' % envelope.rcpt_tos)
        print('Message data:\n')
        print(envelope.content.decode('utf8', errors='replace'))
        print('End of message')
        return '250 Message accepted for delivery'



async def amain(loop):
    try:
        controller = Controller(ExampleHandler(), loop=None, hostname=None, port=8025)
        controller.start()
    except Exception:
        loop.stop()
        sys.exit(0)
        pass
    

def run():
    # start the smtp server on localhost:1025

    print("init")
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.create_task(amain(loop=loop))
    try:
        loop.run_forever()


    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()