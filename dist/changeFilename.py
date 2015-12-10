import shutil
import platform
import os

version = '1.12'
destdir = os.path.join(version, '{0}-{1}'.format(platform.system(), platform.architecture()[0]))
os.makedirs(destdir)
if platform.system() != 'Windows':
    shutil.move('NFsim', os.path.join(destdir, 'NFsim'))
else:
    shutil.move('NFsim.exe', os.path.join(destdir, 'NFsim.exe'))
