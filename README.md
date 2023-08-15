# AAA_The_Dudes

## Execute

To replicate our results please execute the requirements.txt followed by the notebooks in numerical order

## Structure

For clarity and to be able to work together in git on the same topics, we divided the notebooks not only by task, but also into subtasks. The structure is described below:

### 0. Pre-Preparation

- 00_export_hdf5.ipynb: Create a hdf5 file, to work with the large dataset
- 00_weatherdata_scraping.ipynb: Load and prepare the weather data

### 1. Preparation

- 01_prep.ipynb: Prepare the data for analysis

### 2. Descriptive analysis

- 02_demand_Analysis.ipynb: Analysis of demand at differrent levels
- 02_time_Analysis.ipynb: Detailed analysis of the trip length and timepoints
- 02_utilization.ipynb: General analysis of the utilization

### 3. Spacial Analyis

- 03_location.ipynb: Detailed analysis of the spacial data for different topics e.g. demand

### 4. Clustering

- 04_clustering.ipynb: The cluster analysis using K-means++ and GMM

### 5. Prediction

- 05_point_of_interest.ipynb: Loads the point of interest from the overpass api
- 05a_prediction_data_prep.ipynb: Preparation for prediction and feature engeneering
- 05b_nn_prediction.ipynb: Build a predictive model using a neuronal network
- 05c_svm_prediction.ipynb: Build a predicitve model using a support vector machine
- 05d_prediction_results.ipynb: Analysis of the performance of both models

### 6. Reinforcement Learning

- 06_reinforcement_learning.ipynb: An intelligent charging system for an electric vehicle