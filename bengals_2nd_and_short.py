#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import sportsdataverse as sdv


# In[2]:


pbp = sdv.nfl.load_nfl_pbp(seasons=2021)


# In[3]:


pbp.head()


# In[4]:


cin_pbp = pbp[pbp['posteam'] == 'CIN']


# In[5]:


cin_2nd = cin_pbp[(cin_pbp['down'] == 2) & (cin_pbp['yardline_100'] > 20) & (cin_pbp['yardline_100'] < 80)]


# In[6]:


cin_2ndshort = cin_2nd[(cin_2nd['ydstogo'] < 4) & cin_2nd['play_type'].isin(['pass', 'run'])]


# In[7]:


sns.displot(x = 'epa', data = cin_2ndshort)


# In[8]:


worst_play = cin_2ndshort[cin_2ndshort['epa'] == min(cin_2ndshort['epa'])]


# In[9]:


print(worst_play['epa'])


# In[10]:


pd.options.display.max_colwidth = 1000
print(worst_play['desc'])


# In[11]:


no_worst_play = cin_2ndshort[cin_2ndshort['play_id'] != max(worst_play['play_id'])]


# In[12]:


no_worst_play['play_type'].value_counts()


# In[13]:


sns.boxplot(x = 'play_type', y = 'epa', data = no_worst_play).set(title = 'EPA Distribution on 2nd & Short (3 yards or less to go)', xlabel = '', ylabel = 'EPA')
plt.savefig('epa_distribution.png', dpi = 200)

