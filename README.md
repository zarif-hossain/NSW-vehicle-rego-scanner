# NSW-Vehicle-Rego-Scanner

## Getting Started
Run the following commands to install the neccessary libraries:
```
pip install ultralytics
pip install selenium
```
### Development Process:

#### Web Bot:

    1) Install desired browser driver
        - For this project I chose chrome

    2) The web page that I will send the data to is ServiceNSW
        - This means only NSW registrations will be read

#### Machine Learning/Object Detection:

    1) Collect data (Take images or find an online video)
        - I used YouTube from - Dash cam Australia

    2) Use CNVMp3 to download the YouTube video 
        - I ended up taking snippets of the video I downloaded
        - can also use open datasets from https://storage.googleapis.com/openimages/web/index.html

    3) Image annotation:
        - Roboflow
        - CVAT (used for this project)
        - Annotated the images to two labels:
            1) car
            2) rego_plate

    4) 