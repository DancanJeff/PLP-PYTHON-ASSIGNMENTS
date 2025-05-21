# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
def load_and_explore_data():
    try:
        # Load the Iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], 
                         columns=[*iris['feature_names'], 'target'])
        
        # Convert target numbers to species names
        species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        df['species'] = df['target'].map(species_map)
        
        print("First 5 rows of the dataset:")
        print(df.head())
        print("\nDataset Info:")
        print(df.info())
        
        # Check for missing values
        print("\nMissing values:")
        print(df.isnull().sum())
        
        return df
    
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Task 2: Basic Data Analysis
def perform_analysis(df):
    if df is None:
        return
    
    print("\nBasic statistics of numerical columns:")
    print(df.describe())
    
    print("\nMean values by species:")
    print(df.groupby('species').mean())

# Task 3: Data Visualization
def create_visualizations(df):
    if df is None:
        return
    
    # Set style for better visualizations
    sns.set_style("whitegrid")
    
    # Create a figure with subplots
    fig = plt.figure(figsize=(15, 10))
    
    # 1. Line chart - trends of sepal length
    plt.subplot(2, 2, 1)
    plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
    plt.title('Sepal Length Trend')
    plt.xlabel('Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    
    # 2. Bar chart - average petal length per species
    plt.subplot(2, 2, 2)
    sns.barplot(x='species', y='petal length (cm)', data=df)
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    
    # 3. Histogram - sepal width distribution
    plt.subplot(2, 2, 3)
    plt.hist(df['sepal width (cm)'], bins=20)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    
    # 4. Scatter plot - sepal length vs petal length
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', 
                   hue='species', style='species')
    plt.title('Sepal Length vs Petal Length')
    
    plt.tight_layout()
    plt.show()

def main():
    # Execute all tasks
    print("Task 1: Loading and Exploring Data")
    df = load_and_explore_data()
    
    print("\nTask 2: Performing Basic Analysis")
    perform_analysis(df)
    
    print("\nTask 3: Creating Visualizations")
    create_visualizations(df)

if __name__ == "__main__":
    main()
