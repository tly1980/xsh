#!/usr/bin/env python
'''
The MIT License (MIT)

Copyright (c) [2015] [Tom Tang]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
import subprocess
import os
import time

def main():
    argv2 = argv = list(sys.argv[1:])
    host = argv[0]

    dry = True if '--dry' in argv else False

    jump = None
    if '-j' in argv:
        idx = argv.index('-j')
        jump = argv[idx+1]
        # remove the "-j", "jumpbox"
        argv2 = argv[:idx] 
        argv2 += ['-o', 'ProxyCommand="ssh {jump} nc %h %p"'.format(jump=jump)]
        argv2 += argv[idx+2:]

    retry = 50 if '--failfast' not in argv2 else 1

    if 'XSH_USER' in os.environ:
        user = os.environ['XSH_USER']
    else:
        user = None

    if '@' not in host and user:
        host = '%s@%s' % (user, host)

    argv2 = [a for a in argv2[1:] if a not in ['--dry', '--failfast']]

    lst = ['ssh', host] + argv2

    if not dry:
        for i in range(retry):
            cmd = ' '.join(lst)
            print "Try %d/%d: %s" % (i+1, retry, cmd)
            r = subprocess.call(cmd, shell=True)
            if r != 255:
                sys.exit(r)
            print >> sys.stderr, "Sleep for 5 secs ..." 
            time.sleep(5.0)

        sys.exit(r)
    else:
        print "[DRY] Calling: %s" % " ".join(lst)

if __name__ == '__main__':
    main()
