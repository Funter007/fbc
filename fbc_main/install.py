#coding=utf-8
#!/usr/bin/python2

import os
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    from fbc64 import main_fbcx
    main_fbcx()
elif bit == '32bit':
    from fbc32 import main_fbcx
    main_fbcx()
