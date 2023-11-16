#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from textblob import TextBlob

# Load the Excel file into a DataFrame
file_path = r"C:\Users\ksamy\Desktop\CEO thoughts on  AI\CEO thoughts on AI.xlsx"  # Replace with the actual file path
df = pd.read_excel(file_path)


# In[7]:


df.head()


# In[11]:


df.columns


# In[29]:


# Ensure that the "Thoughts on AI" column contains text data
df['THOUGHTS ON AI '] = df['THOUGHTS ON AI '].astype(str)

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Classify the polarity of the text as positive, negative, or neutral
    if analysis.sentiment.polarity > 0.1:
        return 'Positive'
    elif analysis.sentiment.polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'


# In[30]:


# Apply sentiment analysis to the "Thoughts on AI" column and create a new column for sentiment
df['Sentiment'] = df['THOUGHTS ON AI '].apply(analyze_sentiment)

# Display the DataFrame with the added "Sentiment" column
print(df[['TOP COMPANIES IN THE WORLD ', 'CEO NAME ', 'THOUGHTS ON AI ', 'Sentiment']])


# In[31]:


import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have the DataFrame with the "Sentiment" column and "Core of the Company" column
# If not, you should load the data and perform sentiment analysis as shown before

# ----- Sentiment Analysis Chart -----

# Count the number of companies with each sentiment
sentiment_counts = df['Sentiment'].value_counts()

# Plot the sentiment analysis chart
plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
plt.title('Sentiment Analysis of CEOs on AI')
plt.xlabel('Sentiment')
plt.ylabel('Number of Companies')
plt.show()


# In[33]:


# Assuming you have the DataFrame with the "Sentiment" column and "Core of the Company" column
# If not, you should load the data and perform sentiment analysis as shown before

# Group the DataFrame by the "Core of the Company" column
grouped_df = df.groupby('CORE OF THE COMPANY ')

# Initialize a dictionary to store adoption rates for each core
adoption_rates = {}

# Calculate the adoption rate for each core
for core, core_group in grouped_df:
    total_companies_in_core = len(core_group)
    positive_sentiment_companies_in_core = core_group[core_group['Sentiment'] == 'Positive']
    
    adoption_rate = len(positive_sentiment_companies_in_core) / total_companies_in_core * 100
    adoption_rates[core] = adoption_rate

# Print the adoption rates for each core
print("Adoption Rates based on Core of the Company:")
for core, rate in adoption_rates.items():
    print(f"{core}: {rate:.2f}%")


# In[34]:


# ----- Adoption Rate Chart -----

# Assuming you have already calculated adoption rates for each core
# If not, use the previous code snippet to calculate adoption rates

# Create a DataFrame for adoption rates
adoption_df = pd.DataFrame(list(adoption_rates.items()), columns=['Core of the Company', 'Adoption Rate'])

# Sort the DataFrame by adoption rate in descending order
adoption_df = adoption_df.sort_values(by='Adoption Rate', ascending=False)

# Plot the adoption rate chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Adoption Rate', y='Core of the Company', data=adoption_df, palette='coolwarm')
plt.title('Adoption Rate Based on Core of the Company')
plt.xlabel('Adoption Rate (%)')
plt.ylabel('Core of the Company')
plt.show()


# In[35]:


import matplotlib.pyplot as plt

# Assuming you have the DataFrame with the "YEAR" and "MARKET(in millions)" columns
# If not, you should load the data

# Your data
years = [2018,2019,2020,2021,2022,2023,2024,2025]  # Replace with your actual data
market_values = [12566.89,17936.09,25898.12,40121.10,56451.80,79006.57,102033.32,124930.76]  # Replace with your actual data

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(years, market_values, marker='o', linestyle='-')

# Customize the chart
plt.title('Market Growth Over Years')
plt.xlabel('Year')
plt.ylabel('Market (in millions)')
plt.grid(True)
plt.show()


# In[ ]:


import nbformat as nbf
with open(r"C:\Users\ksamy\Desktop\CEO thoughts on  AI\analysis .ipynb") as f:
    nb = nbf.read(f)
nb['cells'] = [cell for cell in nb['cells'] if cell['cell_type'] == 'code']
with open(r"C:\Users\ksamy\Desktop\CEO thoughts on  AI\analysis .py", 'w') as f:
    nbf.write(nb, f)

