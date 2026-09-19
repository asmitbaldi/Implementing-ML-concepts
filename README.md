# Implementing ML Concepts

This repository contains the ML concepts, algorithms, techniques, and experiments
that I have implemented while learning Machine Learning.

Most of the work here is done through Jupyter notebooks, where I try to understand
the concepts by implementing them, experimenting with them, and visualizing the results.

All of the code is handwritten, line by line.

**Note:** This is the organized version of the repository. The original, raw learning
history can be found on the [`main` branch](../../tree/main).

## Topics

### Data Analysis

- [Understanding Data](data_analysis/Understanding_data.ipynb)
- [Univariate Analysis](data_analysis/Univariate.ipynb)
- [Bivariate & Multivariate Analysis](data_analysis/Bivariate_Multivariate.ipynb)
- [Pandas Profiling](data_analysis/Panda_profiling.ipynb)
- [Date & Time](data_analysis/date_and_time.ipynb)
- [Synthetic Datasets](data_analysis/synthetic_datasets.ipynb)
- [Typing Data](data_analysis/typing.ipynb)
- [Teen Mental Health](data_analysis/Teen_mental_health.ipynb)
- [Toy Project](data_analysis/toy_project.ipynb)

### Data Preprocessing

- [Missing Numerical Data](data_preprocessing/Missing_numerical_data.ipynb)
- [Missing Categorical Data](data_preprocessing/missing_categorical_data.ipynb)
- [Random Sample Imputation](data_preprocessing/Random_sample_imputation.ipynb)
- [KNN Imputer](data_preprocessing/KNN_imputer.ipynb)
- [Iterative Imputer](data_preprocessing/IterativeImputer.ipynb)
- [Missing Indicator](data_preprocessing/missing_indicater.ipynb)
- [One-Hot Encoding](data_preprocessing/One_Hot_Encoding.ipynb)
- [Ordinal Encoding](data_preprocessing/Ordianl_Encoding.ipynb)
- [Normalization](data_preprocessing/Normalization.ipynb)
- [Standardization](data_preprocessing/Standardization.ipynb)
- [Function Transformation](data_preprocessing/Function_transformation.ipynb)
- [Power Transformation](data_preprocessing/power_transformation.ipynb)
- [Binning & Binarization](data_preprocessing/binning_&_binarization.ipynb)
- [Handling Mixed Values](data_preprocessing/Handling_Mixed_Values.ipynb)
- [Outlier Detection using IQR](data_preprocessing/Outliner_using_IQR_method.ipynb)
- [Outlier Detection using Z-Score](data_preprocessing/Outliner_using_Z-score.ipynb)
- [Feature Construction](data_preprocessing/feature_construction.ipynb)
- [Imbalanced Data](data_preprocessing/imbalanced_data.ipynb)

### Regression

- [Linear Regression from Scratch](regression/linear_regression_from_scratch.ipynb)
- [Linear Regression using Scikit-learn](regression/linear_regression_using_sklearn.ipynb)
- [Multiple Linear Regression from Scratch](regression/multiple_lr_from_scratch.ipynb)
- [Polynomial Regression](regression/Polynomial_regression.ipynb)
- [Ridge Regularization](regression/Ridge_regularization.ipynb)
- [Ridge - Single Feature from Scratch](regression/Ridge_single_feature_from_scratch.ipynb)
- [Ridge - Multiple Features from Scratch](regression/Ridge_multiple_features_from_scratch.ipynb)
- [Ridge from Scratch using Gradient Descent](regression/Ridge_from_scratch_using_gradient_decent.ipynb)
- [ElasticNet](regression/Elasticnet.ipynb)
- [Linear Regression Assumptions](regression/Linear_reg_assumtions.ipynb)
- [Regression Metrics](regression/regression_metrics.ipynb)
- [Regression Trees](regression/regression_trees.ipynb)

### Classification

- [Logistic Regression](classification/logistic_regression.ipynb)
- [Polynomial Logistic Regression](classification/polynomial_logistic_regression.ipynb)
- [Softmax Regression](classification/softmax_regression.ipynb)
- [K-Nearest Neighbors](classification/KNN.ipynb)
- [Naive Bayes](classification/Naive_Bayes.ipynb)
- [Support Vector Machines](classification/Support_vector_machines.ipynb)
- [Decision Trees](classification/decision_trees.ipynb)

### Ensemble Learning

- [Bagging](ensemble_learning/Bagging.ipynb)
- [Bagging Classifier](ensemble_learning/Bagging_classifier.ipynb)
- [Bagging Regressor](ensemble_learning/Bagging_regressor.ipynb)
- [Random Forest](ensemble_learning/random_forest.ipynb)
- [Voting Classifier](ensemble_learning/voting_classifier.ipynb)
- [Voting Regressor](ensemble_learning/voting_regressor.ipynb)
- [Stacking Ensemble](ensemble_learning/stacking_ensemble.ipynb)
- [AdaBoost from Scratch](ensemble_learning/adaboost_from_scratch.ipynb)
- [Gradient Boosting from Scratch](ensemble_learning/gradient_boosting_from_scratch.ipynb)

### Clustering

- [K-Means Graphical](clustering/kmeans_graphical.ipynb)
- [Agglomerative Clustering](clustering/agglomerative_clustering.ipynb)
- [DBSCAN](clustering/dbscan.ipynb)
- [K-Means Implementation](clustering/KMeans.py)
- [K-Means Usage](clustering/My_KMeans_use.py)

### Dimensionality Reduction

- [PCA](dimensionality_reduction/pca.ipynb)
- [CCA](dimensionality_reduction/CCA.ipynb)

### Gradient Descent

- [Gradient Descent from Scratch](gradient_descent/Gradient_decent_from_scratch.ipynb)
- [Batch Gradient Descent](gradient_descent/batch_gradient_decent.ipynb)
- [Stochastic Gradient Descent](gradient_descent/stochastic_gradient_decent.ipynb)
- [Mini-Batch Gradient Descent](gradient_descent/mini_batch_gradient_decent.ipynb)

### Model Selection

- [GridSearchCV](model_selection/GridSearchCV.ipynb)
- [Optuna](model_selection/optuna.ipynb)

### Pipelines

- [With Pipeline](pipelines/with_pipeline.ipynb)
- [Without Pipeline](pipelines/without_pipeline.ipynb)
- [Column Transformer](pipelines/Column_Transformer.ipynb)
- [Prediction with Pipeline](pipelines/predict_with_pipeline.ipynb)
- [Prediction without Pipeline](pipelines/predict_without_pipeline.ipynb)

### Data Collection

- [Web Scraping](data_collection/Web_scrapping.ipynb)
- [Pokemon Web Scraping](data_collection/Pokemon_web_scraping.ipynb)
- [Working with CSV](data_collection/working_with_csv.ipynb)
- [JSON & SQL](data_collection/Json_sql.ipynb)
- [API](data_collection/Api.ipynb)
- [API - Better Approach](data_collection/Api_better.ipynb)

#### Pokemon Web Scraping Files

- [Pokemon CSV](data_collection/pokemon.csv)
- [Pokemon HTML](data_collection/pokemon.html)
- [Pokemon Output](data_collection/output.html)
- [Pokemon Data](data_collection/pokemon)

## Models

Some of the models I exported from the notebooks are stored in the
[models](models/) directory.

- [Classifier](models/clf.pkl)
- [Pipeline](models/pipe.pkl)
- [Ordinal Encoder - Employment/Other](models/oe_em.pkl)
- [Ordinal Encoder - Sex](models/oe_sex.pkl)

## Datasets

The datasets used in the notebooks are stored separately and are not included
in this repository.

[Dataset Google Drive](https://drive.google.com/drive/folders/1V_OfmLlLFIpp2TiXc--uS12wWOWFECiq?usp=share_link)

## Repository Structure

```text
Implementing-ML-concepts/
│
├── data_analysis/
├── data_preprocessing/
├── regression/
├── classification/
├── ensemble_learning/
├── clustering/
├── dimensionality_reduction/
├── gradient_descent/
├── model_selection/
├── pipelines/
├── data_collection/
├── models/
└── README.md
