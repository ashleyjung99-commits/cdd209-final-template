from src.pharma_adherence.data import PharmaDataset
from src.pharma_adherence.modeling import ModelTrainer

"""
DAY 1: DATA PREPROCESSING & ANALYSIS
"""

# load the dataset
dataset = PharmaDataset("data/raw/prescriptions_large_raw.csv")
print(dataset.df.head())

# Clean the dataset
dataset.clean()

# Save the dataset as a csv into "data/processed/"
dataset.save("data/processed/prescriptions_large_cleaned.csv")

# Visualize the cleaned data against adherence

dataset.hist("sex").show()
dataset.bar("sex", "adherence_flag").show()
dataset.bar("pharmacy_name", "adherence_flag").show()
dataset.bar("prescriber_id", "adherence_flag").show()
dataset.scatter("proportion_days_covered", "adherence_flag").show()
dataset.scatter("copay_amount", "adherence_flag").show()

# Look at the summary of a patient
patient = dataset.get_patient("P057")
print(patient.summary())

"""
DAY 2: MACHINE LEARNING
"""

# Instantiate a linear regression trainer
linear_model = ModelTrainer(dataset.df, target="proportion_days_covered", features=["sex", "copay_amount"])

# Train the linear model
model, metrics = linear_model.train_linear()

# Print the linear model metrics
print(metrics)

# Instantiate a logistic regression trainer
logistic_model = ModelTrainer(dataset.df, "adherence_flag", ["sex", "copay_amount"])

# Train the logistic model
model, metrics = logistic_model.train_logistic()

# Print the logistic model metrics
print (metrics)