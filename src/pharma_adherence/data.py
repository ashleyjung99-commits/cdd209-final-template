from pathlib import Path
import pandas as pd
from .cleaning import clean_prescription_data
from .visualization import plot_hist, plot_bar, plot_scatter
from .patient import PatientAdherenceProfile

class PharmaDataset:
    def __init__(self, filepath):
        self.df = self.load(filepath).copy()
        self.cleaned = False
    
    # load the dataset from a csv file
    def load(self, filepath):
        filepath = Path(filepath)

        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        df = pd.read_csv(filepath)
        return df

    # clean the dataset using the cleaning function
    def clean(self):
        self.df = clean_prescription_data(self.df)
        self.cleaned = True
    
    # save the cleaned dataset to a csv file
    def save(self, filepath):
        if self.cleaned is False:
            raise ValueError("Run clean() first.")
        
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        self.df.to_csv(filepath)
    
    # visualize the dataset using the visualization functions
    def hist(self, column_name):
        if self.cleaned is False:
            raise ValueError("Run clean() first.")
        
        return plot_hist(self.df, column_name, label_rotation=45)
    
    def bar(self, cat, values):
        if self.cleaned is False:
            raise ValueError("Run clean() first.")
        
        return plot_bar(self.df, cat, values, label_rotation=45)
    
    def scatter(self, x, y):
        if self.cleaned is False:
            raise ValueError("Run clean() first.")
        
        return plot_scatter(self.df, x, y)

    # get the adherence profile of a patient given their patient ID
    def get_patient(self, patient_id):
        if self.cleaned is False:
            raise ValueError("Run clean() first.")
        
        patient_df = self.df[
            self.df["patient_id"] == patient_id
        ]

        return PatientAdherenceProfile(patient_id, patient_df)
    
    # gets the dataframe of the dataset
    def get_df(self):
        return self.df
    
    # checks if the dataset has been cleaned
    def is_clean(self):
        return self.cleaned