import struct
import pip

from shutil import copyfile
from os import listdir
from os.path import isfile, join
from os import rename

arch = struct.calcsize("P")*8
if arch == 32:
    files = [f for f in listdir('32-bit/') if isfile(join('32-bit', f))]
    for file in files:
        copyfile(f'32-bit/{file}', file)
else:
    files = [f for f in listdir('64-bit/') if isfile(join('64-bit', f))]
    for file in files:
        copyfile(f'64-bit/{file}', file)
pip.main(['install', "opencv_python==3.4.1.15"])
pip.main(['install', "https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py"])
pip.main(['install', "PyJWT==1.6.4 "])
