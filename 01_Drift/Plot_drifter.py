import pandas as pd
import plotly.express as px
import plotly
import numpy as np 

#reading data frames with pandas
df1e2 = pd.read_csv('./Scripts/02_SteppingStone/driftedPop_Rep10_N100.csv', names=['Generation','Frequency','Replicate'])
df1e3 = pd.read_csv('./Scripts/02_SteppingStone/driftedPop_Rep10_N1000.csv', names=['Generation','Frequency','Replicate'])
df1e4 = pd.read_csv('./Scripts/02_SteppingStone/driftedPop_Rep10_N10000.csv', names=['Generation','Frequency','Replicate'])
df1e5 = pd.read_csv('./Scripts/02_SteppingStone/driftedPop_Rep10_N100000.csv', names=['Generation','Frequency','Replicate'])

#merging all the data frames into a single one
df = pd.concat([df1e2,df1e3,df1e4,df1e5], keys=["Ne=100","Ne=1000","Ne=10000","Ne=100000"]).reset_index()
#df.head()

fig = px.line(df, x = 'Generation', y = 'Frequency', color='level_0', line_group='Replicate', labels={"level_0": ""})
fig.update_xaxes(range=[0, 9900])
fig.update_yaxes(range=[0, 1])
#fig.show()
fig.write_image("./Figures/Drift_python.png")
