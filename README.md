simpleident
===========

This is an indent server that simply replies with the contents of a file (read on every request), 
or with a fixed username.

I created this as a simple companion to the ZNC [identfile](http://wiki.znc.in/Identfile) plugin.

Usage
-----

```
simpleident.py [-h] [--bind BIND] [--port PORT]
               [--system-type SYSTEM_TYPE]
               (--username USERNAME | --file FILE)


-h, --help                 show this help message and exit
--bind BIND                The IP to bind to (default: 0.0.0.0)
--port PORT                The port to bind to (default: 113)
--system-type SYSTEM_TYPE  The system type (default: UNIX)
--username USERNAME        A fixed username to reply with
--file FILE                A file with the username to reply with
```

Example
-------

1. Create a file named `/tmp/ident`
2. Run `python simpleident.py --file /tmp/ident`

Requirements
------------

This program only requires python (2 or 3), without any extra libraries.