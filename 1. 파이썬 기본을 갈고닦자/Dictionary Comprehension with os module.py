import os
import glob
from pprint import pprint as pp

file_info = {os.path.realpath(p) : os.stat(p).st_size for p in glob.glob("*.*")}
pp(file_info)