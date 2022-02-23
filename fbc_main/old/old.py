#coding=utf-8
#!/usr/bin/python2

import os
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    from old64 import loginvia
    loginvia()
elif bit == '32bit':
    from old32 import loginvia
    loginvia()
