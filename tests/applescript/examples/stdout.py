#!/usr/bin/env python
import sys
import applescript

if "darwin" in sys.platform:
    r = applescript.run('return 1')
    print(r.out)
