#!/usr/bin/env python
import applescript
import tests_os.mac


applescript.tell.app("Terminal", 'do script "ls"')
applescript.tell.app("Terminal", 'do script "echo background"',background=True)
