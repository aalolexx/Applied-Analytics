# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 15:03:01 2025

@author: schiltem93
"""
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px


#%%

# Set random seed for reproducibility
np.random.seed(42)

# Generate 200 random x values
x = np.random.normal(0, 1, 200)

# Generate y with medium correlation to x (correlation ~ 0.5)
y = 0.5 * x + np.random.normal(0, 1, 200)

# Generate z with medium correlation to x (correlation ~ 0.5)
z = 0.5 * x + np.random.normal(0, 1, 200)

# Shuffle z values randomly to ensure no correlation between y and z
np.random.shuffle(z)

# Create DataFrame
df = pd.DataFrame({'x': x, 'y': y, 'z': z})

# Display correlation matrix
print(df.corr())

#%%


# Create interactive 3D scatter plot
fig = px.scatter_3d(df, x='x', y='y', z='z', opacity=0.7, title="Interactive 3D Scatter Plot")

# Show plot
fig.show()