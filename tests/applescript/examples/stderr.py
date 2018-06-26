#!/usr/bin/env python
import sys
import applescript

if "darwin" in sys.platform:
    r = applescript.run('log "hello world"')
    print(r.err)
