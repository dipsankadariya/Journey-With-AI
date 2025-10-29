# Iris Dataset

The Iris dataset contains 150 samples of iris flowers from three species: Setosa, Versicolour, and Virginica. Each sample has 4 features: sepal length, sepal width, petal length, and petal width. It is widely used for classification tasks in machine learning.

You can load the dataset using scikit-learn:

```python
from sklearn.datasets import load_iris

data = load_iris()
X = data.data
y = data.target
