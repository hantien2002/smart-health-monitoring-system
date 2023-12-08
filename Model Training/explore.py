# Before starting with the model development, we will first familiarize with the dataset. 
# Understand its structure, what each column represents, and any preprocessing needed.

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
plt.style.use('ggplot')
# pd.set_option('max_columns', 200)

heart_rate_df = pd.read_csv('/Users/tien/Desktop/Smart_HMS/smart-health-monitoring-system/Model Training/Kaggle Data/heart_rate_data.csv')

