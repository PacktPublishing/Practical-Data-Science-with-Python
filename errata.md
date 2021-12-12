# Errata & Improvements

If you find any mistakes in the book orhave suggestions for improvements, then please raise an issue in this repository contact me through LinkedIn or email.

## Page 545

The code sample was put into the book incorrectly, it should be:

```python
feature_importances = 
pd.Series(lgbm.feature_importances_,

index=pyclf.get_config('X').columns)

feat_imp_plot = 
feature_importances.nlargest(20).plot(kind='barh')

feat_imp_plot.invert_yaxis()
```

In the book, `feat_imp_` is incorrectly moved to the end of the second line.