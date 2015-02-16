#!/usr/bin/env python
import argparse
try:
    import SocketServer  # Python 2
except ImportError:
    import socketserver as SocketServer # Python 3


def main(args):
    # Start Server
    class IdentHandler(SocketServer.BaseRequestHandler):
        def handle(self):
            username = args.username
            if args.file:
                with open(args.file.name, args.file.mode) as f:
                    username = f.read().strip()

            data = self.request.recv(1024)

            if username.strip() == "":
                reply = "%s: ERROR : NO-USER\r\n"
            else:
                reply = "%s : USERID : %s : %s\r\n" % (data.strip().replace('\b', ''), args.system_type, username)

            self.request.sendall(reply)
            print("Replied to %s: \"%s\"" % (self.client_address[0], reply.strip()))

    server = SocketServer.TCPServer((args.bind, args.port), IdentHandler)

    try:
        server.serve_forever()
    finally:
        server.server_close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Runs an ident server that replies with data from a file, or with a fixed username.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Network options
    parser.add_argument('--bind', type=str, default="0.0.0.0", help="The IP to bind to")
    parser.add_argument('--port', type=int, default=113, help="The port to bind to")

    # Ident options
    parser.add_argument('--system-type', type=str, default="UNIX", help="The system type")
    name_group = parser.add_mutually_exclusive_group(required=True)
    name_group.add_argument('--username', type=str, help="A fixed username to reply with")
    name_group.add_argument('--file', type=argparse.FileType('r'), help="A file with the username to reply with")

    # Parse args and run server
    main(parser.parse_args())
