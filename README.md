# Practical-Data-Science-with-Python
This is the code repository for [Practical Data Science with Python](), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.

## About the Book
---

## Instructions and Navigation
The code from this book and repository is intended for Python 3.9. The `datasci.yml` file can be used to create a conda virtual environment by running `conda env create -f datasci.yml`. The conda environment can then be activated with `conda activate datasci`.


All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
>>> from sklearn.neighbors import KNeighborsClassifier
>>> knn = KNeighborsClassifier(n_neighbors=5, p=2,
... metric='minkowski')
>>> knn.fit(X_train_std, y_train)
>>> plot_decision_regions(X_combined_std, y_combined,
... classifier=knn, test_idx=range(105,150))
>>> plt.xlabel('petal length [standardized]')
>>> plt.ylabel('petal width [standardized]')
>>> plt.show()
```

## Related Products
* [Python Machine Learning](https://www.packtpub.com/big-data-and-business-intelligence/python-machine-learning?utm_source=github&utm_medium=repository&utm_campaign=9781783555130)

* [Python: End-to-end Data Analysis](https://www.packtpub.com/big-data-and-business-intelligence/python-end-end-data-analysis?utm_source=github&utm_medium=repository&utm_campaign=9781788394697)

* [Python: Real World Machine Learning](https://www.packtpub.com/big-data-and-business-intelligence/python-real-world-machine-learning?utm_source=github&utm_medium=repository&utm_campaign=9781787123212)



## add to datasci.yml file
- pip:
    - pandas-profiling
    - matplotlib-label-lines