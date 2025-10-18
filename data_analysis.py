# Simple Data Analysis Demo
# My First GitHub Python File

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_data():
    """A simple function to demonstrate data analysis skills"""
    
    # Create sample data
    print("Creating sample data...")
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [150, 200, 175, 300, 250],
        'Expenses': [100, 120, 110, 140, 130]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    print("\nSales Data:")
    print(df)
    
    # Basic calculations
    total_sales = df['Sales'].sum()
    average_expenses = df['Expenses'].mean()
    
    print(f"\nTotal Sales: ${total_sales}")
    print(f"Average Expenses: ${average_expenses:.2f}")
    
    # Calculate profit
    df['Profit'] = df['Sales'] - df['Expenses']
    print(f"\nTotal Profit: ${df['Profit'].sum()}")
    
    return df

if __name__ == "__main__":
    results = analyze_data()
