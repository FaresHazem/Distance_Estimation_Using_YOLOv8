# CrocoMarine Training Final Project: Distance Estimation Using YOLOv8

**Made by: Fares Hazem Mohamed Shalaby**

## Table Of Contents
1. [Introduction](#introduction)
2. [Data Collection](#data-collection)
3. [YOLOv8 Model Training](#yolov8-model-training)
4. [Applying YOLOv8 Model on Real-time Camera](#applying-yolov8-model-on-real-time-camera)
5. [Distance Estimation Algorithm Implementation](#distance-estimation-algorithm-implementation)
6. [Integration of All Components](#integration-of-all-components)
7. [Project Structure](#project-structure)

## Introduction

In this project, the goal is to implement a distance estimation system between a real-time camera and a designated 15x15 square, referred to as a "box," detected by the YOLOv8 model. The project showcases the practical application of object detection and distance estimation in a real-world scenario.

## Data Collection

For data collection, multiple datasets were created and experimented with to improve the quality of the dataset. The challenges faced and the final dataset selection are detailed in this section.

## YOLOv8 Model Training

The YOLOv8 model training involved experimentation with different models, data augmentation, and preprocessing techniques. The challenges faced and the optimization steps taken to achieve satisfactory results are documented.

## Applying YOLOv8 Model on Real-time Camera

After successfully training the YOLOv8 model, the next step involved applying the model to a real-time camera feed. Challenges and adjustments made during this process are discussed.

## Distance Estimation Algorithm Implementation

The distance estimation algorithm is implemented using a specific formula, and adjustments made to ensure accurate estimations are detailed. Initial tests and fine-tuning procedures are also discussed.

## Integration of All Components

This section covers the integration of the YOLOv8 algorithm, distance estimation formula, and real-time camera functionality. Challenges faced during integration and the steps taken to enhance user experience are documented.

## Project Structure

The project folder is named "Distance_Estimation_Using_YOLOv8" and consists of the following folders:

- **Code**: Contains Python scripts for various functionalities, including live video streaming, distance estimation, and focal length calculation.
  - [Applying YOLOv8 Model On Live Video Stream.py](Code/Applying%20YOLOv8%20Model%20On%20Live%20Video%20Stream.py)
  - [Distance Estimation from Live Video Stream.py](Code/Distance%20Estimation%20from%20Live%20Video%20Stream.py)
  - [Distance Estimation Using a Picture.py](Code/Distance%20Estimation%20Using%20a%20Picture.py)
  - [Focal Length Calculation.py](Code/Focal%20Length%20Calculation.py)
  - [Size of Black Square in Pixels.py](Code/Size%20of%20Black%20Square%20in%20Pixels.py)
  - [Video Capturing Using Webcam.py](Code/Video%20Capturing%20Using%20Webcam.py)
  - **Images**: Folder containing images used for testing, including [img.jpg](Code/Images/img.jpg).
  - **Models**: Folder containing trained models, including [best.pt](Code/Models/best.pt), [yolov8m.pt](Code/Models/yolov8m.pt), and [yolov8n.pt](Code/Models/yolov8n.pt).

- **Data**: Contains datasets used for training and testing the YOLOv8 model, as well as images used in the datasets.
  - **Datasets**: Folder containing trial datasets, each with train, test, and valid folders and [data.yaml](Data/Datasets/Dataset%20(Trial%201)/data.yaml) file.
    - [Dataset (Trial 1)](Data/Datasets/Dataset%20(Trial%201))
    - [Dataset (Trial 2)](Data/Datasets/Dataset%20(Trial%202))
    - [Dataset (Trial 3)](Data/Datasets/Dataset%20(Trial%203))
    - [Dataset (Trial 4)](Data/Datasets/Dataset%20(Trial%204))
    - [Dataset (Trial 5)](Data/Datasets/Dataset%20(Trial%205))
  - **Images**: Folder containing images used to create datasets, including [Images (Trial 1)](Data/Images/Images%20(Trial%201)), [Images (Trial 2)](Data/Images/Images%20(Trial%202)), and [Images (Trial 3)](Data/Images/Images%20(Trial%203)).

- **Documentation**: Contains editable and read-only documentation files, including a PowerPoint presentation, a timeline, and an editable document.
  - **Editable**: Folder containing editable documentation files.
    - [Documentation.docx](Documentation/Editable/Documentation.docx)
    - [Presentation.pptx](Documentation/Editable/Presentation.pptx)
    - [Timeline.xlsx](Documentation/Editable/Timeline.xlsx)
    - **Template**: Folder containing the template used for PowerPoint, [Aliena · SlidesCarnival.pptx](Documentation/Editable/Template/Aliena%20·%20SlidesCarnival.pptx).
  - **Images**: Folder containing images used in the documentation, including [1.jpg](Documentation/Images/1.jpg), [2.png](Documentation/Images/2.png), [3.png](Documentation/Images/3.png), and [YOLOv8.png](Documentation/Images/YOLOv8.png).
  - **Read Only**: Folder containing read-only documentation files, including [Documentation.pdf](Documentation/Read%20Only/Documentation.pdf) and [Presentation.ppsx](Documentation/Read%20Only/Presentation.ppsx).

- **Notebooks**: Contains Jupyter notebooks used for YOLOv8 custom object detection using Google Colab and Kaggle.
  - [YOLOv8 Custom Object Detection Using Google Colab.ipynb](Notebooks/YOLOv8%20Custom%20Object%20Detection%20Using%20Google%20Colab.ipynb)
  - [YOLOv8 Custom Object Detection Using Kaggle.ipynb](Notebooks/YOLOv8%20Custom%20Object%20Detection%20Using%20Kaggle.ipynb)