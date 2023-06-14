import os
import shutil

import SimpleHTR.src.main
import WordDetectorNN.src.infer
from WordDetectorNN import *
from SimpleHTR import *

temp_folder = WordDetectorNN.src.infer.main(path_to_test_folder='../data/test')
if temp_folder:
    SimpleHTR.src.main.main(temp_folder, True)
else:
    raise FileExistsError


shutil.rmtree(temp_folder)
print(f"Deleted folder: {temp_folder}")