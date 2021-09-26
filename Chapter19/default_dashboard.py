import phik
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import pycaret.classification as pyclf
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

st.set_page_config(layout="wide")

# load data
df = pd.read_excel('data/default of credit card clients.xls',
                    skiprows=1,
                    index_col='ID').sample(1000)

setup = pyclf.setup(df, target='default payment next month', silent=True)
lgbm = pyclf.create_model('lightgbm')
lgbm, tuner = pyclf.tune_model(lgbm, return_tuner=True)

cv_acc = round(tuner.cv_results_['mean_test_score'].mean(), 3)
st.title(f"CV Accuracy is {cv_acc}")

# EDA plots
phik_corr = df.phik_matrix()
correlogram = sns.heatmap(phik_corr)

barchart = px.histogram(df,
                        x='PAY_0',
                        color='default payment next month',
                        barmode='group')

col1, col2 = st.columns(2)
col1.write(correlogram.figure)
col2.write(barchart)
plt.clf()

# feature importance plot
feature_importances = pd.Series(lgbm.feature_importances_,
                                index=pyclf.get_config('X').columns)
feat_imp_plot = feature_importances.nlargest(20).plot(kind='barh')
feat_imp_plot.invert_yaxis()

col1, col2 = st.columns(2)
col1.write(feat_imp_plot.figure)

# confusion matrix plot
predictions = pyclf.predict_model(lgbm, df)
cm = plot_confusion_matrix(
    confusion_matrix(df['default payment next month'],
    predictions['Label'])
    )

col2.write(cm[1].figure)
