# Image Mosaic - WebApp

This is the a Mosaicking WebApp created during the study week [*Fascinating Informatics*](https://sjf.ch/) from 9.-13. Sept. 2019 at the University of Bern.

## Installation

You require Python version 3.6 or higher.
Create a virtual environment (e.g. in your home folder) and activate it:
```
virtualenv ~/venvs/mosaic
source ~/venvs/mosaic/bin/activate
pip install -r requirements.txt
```

## Running The Django WebApp

### Initial setup
```
source ~/venvs/mosaic/bin/activate
python manage.py migrate
```

### Running the server
```
source ~/venvs/mosaic/bin/activate
python manage.py runserver
```

## Acknowledgements
This WebApp is the result of the study week "Fascinating Informatics", organized by the Swiss Youth in Science foundation. 
Students who participated in this project:
- Elina Teplygina
- Marlon Anderes
- Simon Schedes

Coordinator: Prof. Dr. Paolo Favaro

Tutor: Adrian Wälchli

Funded by the Hasler Stiftung
