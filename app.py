import streamlit as st
import plotly.express as px
from scipy.signal import savgol_filter
import pandas as pd

st.title("Inverse Dissolution - gladilec linij")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
  # Get list of column names
  column_names = df.columns
   

#Add sliders for window length and polynomial order
window_length = st.slider('Window length', 3, 18)

if window_length == 20:
    polyorder = st.slider('Polynomial order', 1, 17)
else:
    polyorder = st.slider('Polynomial order', 1, window_length - 1)

# Apply Savitzy-Golay filter to each column
for column in column_names:
    df[column] = savgol_filter(df[column], window_length, polyorder)

# Create plotly figure
fig = px.line(df,
              x=df.index,
              y=column_names,
              )

fig.update_layout(
    xaxis_title="čas (min)",
    yaxis_title="",
    legend_title="Legenda",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="Black"
    )
)

st.plotly_chart(fig, use_container_width=True)