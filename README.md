# DashGC
This is a simple approach to Gesture Recognition using Deep learning in tensorflow. This uses a combination of Convolutional Neural Networks & variant of Recurrent Neural Network for recognising the hand and the movement (gesture) made using it respectively. 

The recognised gestures are then (planned to be) mapped to actual Desktop controls to allow Gesture Control. The client program uses simple API requests to the deployed flask server.

### Function Map
| Gesture | Function |
| ------- | -------- |
| Doing other things | Nothing |
| Drumming Fingers | TBD |
| No gesture | Waiting |
| Pulling Hand In | TBD |
| Pulling Two Fingers In | TBD |
| Pushing Hand Away | TBD |
| Pushing Two Fingers Away | TBD |
| Rolling Hand Backward | TBD |
| Rolling Hand Forward | TBD |
| Shaking Hand | TBD |
| Sliding Two Fingers Down | TBD |
| Sliding Two Fingers Left | TBD |
| Sliding Two Fingers Right | TBD |
| Sliding Two Fingers Up | TBD |
| Stop Sign | TBD |
| Swiping Down | TBD |
| Swiping Left | TBD |
| Swiping Right | TBD |
| Swiping Up | TBD |
| Thumb Down | TBD |
| Thumb Up | TBD |
| Turning Hand Clockwise | TBD |
| Turning Hand Counterclockwise | TBD |
| Zooming In With Full Hand | TBD |
| Zooming In With Two Fingers | TBD |
| Zooming Out With Full Hand | TBD |
| Zooming Out With Two Fingers | TBD |


## Development

### Requirements
 - Python3
 - tensorflow
 - Jupyter Notebook

### Setup
 1. `$ pip install -r requirements`
 2. `$ jupyter notebook`
 3. Download the original dataset from [here](https://20bn.com/datasets/jester). 
 4. Copy it onto your local machine or google drive.

    **NOTE:** This repository was originally run in a free Google Colab VM environment.

 5. Run the Preprocessing notebook after tweaking the paths & removng google drive mount if running locally.
 6. Run the Data Loading notebook to start working on it.

---

 ## Getting started on Deploying it
 This is a Work-in-Progress, will be updated once the model has been trained & tested.
