# Before installation make sure the access to the GPU

!nvidia-smi

import os
HOME = os.getcwd()
print(HOME)

# Installing YOLOv8

# Pip install method (recommended)
!pip install ultralytics==8.0.20

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

# Git clone method (for development)
# %cd {HOME}
# !git clone github.com/ultralytics/ultralytics
# %cd {HOME}/ultralytics
# !pip install -e .

# from IPython import display
# display.clear_output()

# import ultralytics
# ultralytics.checks()

from ultralytics import YOLO
from IPython.display import display, Image
