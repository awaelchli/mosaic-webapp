# Image Mosaic - Schweizer Jugend Forscht

This is the basecode for the study week [*Schweizer Jugend Forscht*](https://sjf.ch/) at University of Bern.

## Installation

You require Python version 3.6 or higher.
Create a virtual environment (e.g. in your home folder) and activate it:
```
virtualenv ~/venvs/mosaic
source ~/venvs/mosaic/bin/activate
```
Install PyTorch for your platform by following the instructions [here](https://pytorch.org/).
Choose the CUDA installation if you have a GPU that supports it. 
Install the rest of packages with pip:
```
pip install -r requirements.txt
```

## Jupyter Notebook

Remember to always activate your environment before working on the project. 
To view and edit the notebooks, run the Jupyter server:
```
source ~/venvs/mosaic/bin/activate
jupyter notebook
```
This should open a new tab in your default internet browser. 
If not, copy the url displayed in the terminal and paste it manually into the browser.

## Assignments

You can find a detailed description of the assignments in the project folder.
