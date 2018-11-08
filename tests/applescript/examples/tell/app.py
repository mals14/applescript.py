#!/usr/bin/env python
import applescript
import mac_only


applescript.tell.app("Terminal", 'do script "ls"')
applescript.tell.app("Terminal", 'do script "echo background"',background=True)
