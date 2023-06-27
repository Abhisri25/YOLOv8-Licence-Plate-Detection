!mkdir {HOME}/datasets
%cd {HOME}/datasets

# to install dependencies 
!pip install roboflow --quiet

# importing Roboflow 
from roboflow import Roboflow

# self-generated API Key after creating the project and uploading the dataset in Roboflow 
rf = Roboflow(api_key="GtSZn0tLpPwtP88QkiDK")
project = rf.workspace().project("yolov8-number-plate-detection")
model = project.version(1).model
