#!/usr/bin/env python
import os
import only
from public import public
import runcmd
import temp


def _flags(flags=None):
    if not flags:
        return []
    if isinstance(flags, list):
        return ["-s"] + flags
    return ["-s", flags]


@only.osx
@public
def run(applescript, flags=None, background=False):
    path = applescript
    if not os.path.exists(applescript):  # source code
        path = temp.tempfile()
        open(path, "w").write(applescript)
    cmd = ["osascript", path] + _flags(flags)
    return runcmd.run(cmd, background=background)
