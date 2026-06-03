# Medication Adherence Analysis and Prediction

## Features

- Data cleaning
- Linear regression
- Logistic regression
- Patient summary profile
- Visualize patient adherence data
- Unit tests
- Machine learning models

## Installation

### Clone The Repository

```
git clone git@github.com:ashleyjung99-commits/cdd209-final-template.git
```

### Create A Virtual Environment

```
conda create --name [myenv]
conda activate [myenv]
```

### install the package

```
cd cdd209-final-template
pip install .
```

## Usage
Hit the run button in main.py or in the terminal, type:

```
python main.py
```

You can create different graphs by changing the parameters in the main.py file. You can also look at the summary of a patient by changing the patient ID in the main.py file. This way you can explore the data and see how the different features affect the adherence of the patients.

## Testing

After installation, in repo folder type:
```
pytest
```
Failing tests will be printed in the terminal. You can also run a specific test file by typing:
```
pytest tests/test_[file_name].py
```