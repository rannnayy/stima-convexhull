# stima-convexhull
 Tugas Kecil IF2211 Strategi Algoritma

## Description
Python implementation of convex hull algorithm using quickhull algorithm implementing divide and conquer method introduced in
<b>Anany V. Levitin. 2002. <i>Introduction to the Design and Analysis of Algorithms</i>. Addison-Wesley Longman Publishing Co., Inc., USA.</b>. </br>
This implementation of convex hull algorithm can be used to test whether a set of data are linearly separable. If in the plotting, convex hulls of different data doesn't overlap each other, then the two are linearly separable.

## Algorithm Overview
This code is built using <i>Divide and Conquer</i> strategy as follows:
1. Data Preparation
    * Number all points that are going to be processed
    * Sort points by X-axis ascending. If there are same X-axis values, sort by Y-axis, also ascending 
2. Process
    * Start with 2 points, namely p1 and pn, which are leftmost and rightmost points on sorted array.
    * Return p1 and pn as convex hull constructor if there are no points left to be processed.
    * Divide points based on the area they're in, divided by line p1pn, namely left and right.
    * Call recursive function below to process and add pair of points constructing the convex hull, each for left side points and right side points clustered previously.
    * Return pairs of points constructing the hull.
3. Recursion
    * Return p1 and pn as convex hull constructor if there are no points left to be processed.
    * Search for farthest point to p1pn line, named pmax. If there are several points with same distance, choose the one that maximizes angle between p1pmaxpn.
    * If pmax is found, divide the points again according to line p1pmax and pmaxpn.
    * Ignore points inside p1pmaxpn triangle since they impossibly form the convex hull. To do this, for left side points, only take left ones. Same thing to right side.
    * Repeat recursion for points chosen for each side until there are no points left to be processed.
    * Return simplices forming the convex hull.
4. Output
    * The output for this library is simplices in form of two-dimensional Numpy array containing pairs of indexes of points forming the hull.
The input for this library is a dataset, either self-made in form of list of lists or dataset of your likings, including datasets provided by Scikit-learn.

## Getting Started
### Dependencies
* python3 (I made this using Python 3.10.0)
* jupyter notebook
* pyvenv (optional. It will be fine if you're not using virtual environment, but installing the rest of the libraries are compulsory)
* numpy
* pandas
* sklearn
* matplotlib

### Installing
* Clone this repository, or
* Download as zip

### Executing program
* Make sure you have installed library dependencies listed above
* Open in any text editor
* Select Python3 as the interpreter
* Run myConvexHull.ipynb with Python3 and Jupyter Notebook.

### How to use myConvexHull on your other projects?
* Copy/download myConvexHull.py to your workspace
* Import the library using this line of code:
```
from myConvexHull import myConvexHull
```
* Feed two columns of dataset (or two-dimensional array) of numerical points to the library using this line of code:
```
hull = myConvexHull(yourdata)
```
* Do replace yourdata with your data. Hull is the return variable that will contain simplices (two dimensional array) of the points' indexes in pair.
* You can directly visualize the result using matplotlib.

## Authors
Maharani Ayu Putri Irawan - 13520019 - K01
[@rannnaayy](https://github.com/rannnayy)

## Acknowledgments
<h4>
<ul>
    <li>Munir, R., Maulidevi, N. U. 2022. <i>Algoritma Divide and Conquer (Bagian 4)</i>. Bahan Kuliah IF2211 Strategi Algoritma.</li>
    <li>Anany V. Levitin. 2002. <i>Introduction to the Design and Analysis of Algorithms</i>. Addison-Wesley Longman Publishing Co., Inc., USA.</li>
    <li>Scikit-Learn Toy Datasets Webpage. Accessed from: <a href="https://scikit-learn.org/stable/datasets/toy_dataset.html#linnerrud-dataset" alt="Scikit-Learn Toy Datasets Webpage">https://scikit-learn.org/stable/datasets/toy_dataset.html#linnerrud-dataset</a> on 27 February 2022.</li>
</ul>
</h4>