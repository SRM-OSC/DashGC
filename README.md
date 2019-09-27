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

 5. Run the Preprocessing notebook after tweaking the paths & removing google drive mount if running locally.
 6. Run the Data Loading notebook to start working on it.

### Jupyter Notebook local settings
 - [`Jupytertheme`](https://github.com/dunovank/jupyter-themes) module used for saving myself from default light theme bleeding eye damage.

    ```pip install jupyterthemes```
    ```jt -t monokai -nf latosans -nfs 13 -f source -fs 11 -T -N -kl```

 - Notebook extensions from contrib, [`jupyter_contrib_nbextensions`](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) module used to add certain IDE like functionality to Jupyter Notebook.

    ```pip install jupyter_contrib_nbextensions```

    ```jupyter contrib nbextension install```

     Add the following extensions (for convenience):
     1. Hinterland
     2. Snippets
     3. Split Cells Notebook
     4. Table of Content
     5. Collapsible Headings
     6. Autopep8
 - Widgets [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) enables dashboard like controllers

    ```pip install ipywidgets```

    ```jupyter nbextension enable --py widgetsnbextension```

---

 ## Getting started on Deploying it
 This is a Work-in-Progress, will be updated once the model has been trained & tested.
 
