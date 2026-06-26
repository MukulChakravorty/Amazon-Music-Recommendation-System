# 🎵 Amazon Music Clustering using K-Means

An end-to-end Unsupervised Machine Learning project that segments Amazon Music tracks into meaningful clusters using K-Means Clustering, Principal Component Analysis (PCA), and business-driven insights.

---

## 📌 Project Overview

This project analyzes Amazon Music track data and groups similar songs into meaningful clusters based on their audio characteristics and popularity metrics. By applying K-Means Clustering, the project uncovers hidden patterns in the dataset without using predefined labels.

The workflow includes data preprocessing, exploratory data analysis, feature engineering, feature scaling, cluster evaluation, PCA visualization, and business interpretation. The final output can support recommendation systems, music catalog organization, listener segmentation, and business decision-making.

## 🚀 Live Demo

Experience the deployed application and explore the complete Machine Learning workflow in real time.

**Live Application:** https://amazon-music-clustering.streamlit.app/

The application allows users to adjust 18 audio features, predict the most suitable music category using a trained K-Means clustering model, and receive an interactive recommendation through a professional Streamlit interface.


## 🎯 Business Problem

Online music platforms contain millions of tracks with diverse audio characteristics, making it difficult to organize songs and provide personalized recommendations. Without predefined labels, identifying meaningful groups of similar songs becomes a challenging task.

This project addresses this problem by applying Unsupervised Machine Learning to automatically discover hidden patterns in Amazon Music data. The resulting clusters can be used to improve music recommendation systems, listener segmentation, playlist generation, and catalog management.


## 🎯 Project Objectives

The primary objectives of this project are:

- Clean and preprocess the Amazon Music dataset.
- Perform Exploratory Data Analysis (EDA) to understand feature distributions.
- Engineer meaningful features for clustering.
- Standardize numerical features using feature scaling.
- Determine the optimal number of clusters using the Elbow Method.
- Segment songs using the K-Means Clustering algorithm.
- Evaluate clustering quality using Silhouette Score and Davies-Bouldin Index.
- Visualize cluster separation using Principal Component Analysis (PCA).
- Interpret clusters through business insights and assign meaningful cluster names.
- Export the trained model and clustered dataset for deployment.

## 📂 Dataset Information

| Attribute | Details |
|-----------|---------|
| Dataset Name | Amazon Music Dataset |
| Machine Learning Type | Unsupervised Learning |
| Algorithm Used | K-Means Clustering |
| Records | 95,837 Music Tracks |
| Features Used | 18 Numerical Features |
| Target Variable | None (Unsupervised Learning) |

### Features Used

- Popularity Score
- Duration
- Explicit Content
- Danceability
- Energy
- Key
- Loudness
- Mode
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Tempo
- Time Signature
- Followers
- Artist Popularity
- Release Year


## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python 3 |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Clustering Algorithm | K-Means |
| Dimensionality Reduction | Principal Component Analysis (PCA) |
| Model Evaluation | Elbow Method, Silhouette Score, Davies-Bouldin Index |
| Development Environment | Jupyter Notebook, Visual Studio Code |
| Version Control | Git & GitHub |
| Deployment | Streamlit (Planned) |


## 📁 Project Structure

```
Project_4/
│
├── app/
├── assets/
├── data/
│   └── single_genre_artists.csv
│
├── notebooks/
│   ├── Amazon_Music_Clustering.ipynb
│   ├── Amazon_Music_Clustered.csv
│   └── kmeans_music_model.pkl
│
├── output/
├── plots/
├── README.md
└── requirements.txt
```


## ⚙️ Machine Learning Workflow

The project follows a complete end-to-end Machine Learning pipeline:

```
Raw Dataset
      │
      ▼
Data Understanding
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis (EDA)
      │
      ▼
Feature Engineering
      │
      ▼
Feature Scaling (StandardScaler)
      │
      ▼
Optimal Cluster Selection (Elbow Method)
      │
      ▼
K-Means Clustering
      │
      ▼
Cluster Evaluation
(Silhouette Score & Davies-Bouldin Index)
      │
      ▼
Dimensionality Reduction (PCA)
      │
      ▼
Cluster Visualization
      │
      ▼
Business Insight Generation
      │
      ▼
Cluster Naming
      │
      ▼
Export Dataset & Save Model
```

### Workflow Summary

- Loaded and explored the Amazon Music dataset.
- Cleaned and prepared the dataset for clustering.
- Performed feature engineering to create meaningful variables.
- Applied feature scaling to normalize numerical features.
- Determined the optimal number of clusters using the Elbow Method.
- Built a K-Means clustering model.
- Evaluated clustering performance using Silhouette Score and Davies-Bouldin Index.
- Reduced dimensionality using PCA for visualization.
- Visualized cluster separation in two-dimensional space.
- Interpreted each cluster and assigned business-friendly names.
- Exported the clustered dataset and saved the trained model.


## 📊 Exploratory Data Analysis (EDA)

Before building the clustering model, a detailed Exploratory Data Analysis (EDA) was performed to understand the dataset and identify potential data quality issues.

### EDA Activities

- Examined dataset shape and feature information.
- Checked data types for all variables.
- Identified missing values.
- Removed duplicate records.
- Generated descriptive statistics.
- Analyzed feature distributions.
- Explored numerical and categorical variables.
- Studied feature relationships using visualizations.
- Prepared the dataset for feature engineering.

### Key Observations

- The dataset contains music-related audio features, popularity metrics, artist information, and genre details.
- Numerical features have different value ranges, making feature scaling necessary.
- Duplicate records were removed to improve clustering quality.
- Feature engineering improved the dataset by extracting useful information such as release year.
- The cleaned dataset became suitable for unsupervised learning.


## 🛠️ Feature Engineering

Feature Engineering was performed to improve the quality of the dataset before clustering.

### Techniques Applied

- Extracted release year from release date.
- Removed unnecessary columns.
- Selected meaningful numerical features.
- Preserved important categorical information such as genres.
- Prepared the final feature set for clustering.

### Outcome

The engineered features provided better representation of music characteristics and improved clustering performance.


## 📈 Model Evaluation & Visualization

The clustering model was evaluated using multiple techniques to ensure meaningful segmentation and clear separation among clusters.

### Evaluation Techniques

- **Elbow Method** was used to determine the optimal number of clusters.
- **Silhouette Score** measured how well each data point fits within its assigned cluster.
- **Davies-Bouldin Index** evaluated the similarity between clusters.
- **Principal Component Analysis (PCA)** reduced the dataset into two dimensions for visualization.
- **Cluster Profiling** compared feature averages across all clusters.
- **Normalized Heatmap** highlighted the relative importance of features in each cluster.

### Visualizations Included

- Elbow Curve
- PCA Scatter Plot
- Cluster Comparison Bar Chart
- Cluster Profiling Table
- Normalized Heatmap

These visualizations provide an intuitive understanding of cluster separation and feature characteristics.


## 🎯 Business Insights & Cluster Interpretation

The K-Means algorithm segmented the Amazon Music dataset into four meaningful music groups based on audio characteristics, popularity, artist influence, and release period.

### 🎵 Cluster 1 – Popular Modern Hits

- High song popularity
- High danceability and energy
- Recently released songs
- Represents trending and commercially successful music

### 🎧 Cluster 2 – Mainstream Songs

- Balanced audio characteristics
- Moderate popularity
- Broad audience appeal
- Represents the largest music segment in the dataset

### 🌟 Cluster 3 – Artist-Driven Classics

- High artist popularity
- Older but well-recognized songs
- Popular due to artist reputation rather than recent trends

### 🎼 Cluster 4 – Vintage Acoustic Tracks

- High acousticness
- Lower energy and popularity
- Contains older songs with niche audience appeal

### Business Applications

The identified clusters can support:

- Personalized Music Recommendation Systems
- Playlist Generation
- Audience Segmentation
- Music Catalog Organization
- Content Strategy and Promotion
- User Preference Analysis


## 📊 Project Results

The project successfully segmented **95,837 Amazon Music tracks** into **four meaningful clusters** using the K-Means Clustering algorithm.

The clustering quality was evaluated using the Elbow Method, Silhouette Score, and Davies-Bouldin Index. PCA visualization confirmed meaningful cluster separation, while cluster profiling and normalized heatmaps provided clear business interpretation.

The final outputs include a clustered dataset, trained machine learning model, and comprehensive project documentation ready for deployment and future integration into recommendation systems.


## 📂 Project Deliverables

The following deliverables were generated as part of this project:

- 📓 Complete Jupyter Notebook (`Amazon_Music_Clustering.ipynb`)
- 📊 Clustered Dataset (`Amazon_Music_Clustered.csv`)
- 🤖 Trained K-Means Model (`kmeans_music_model.pkl`)
- 📈 Data Visualizations (Elbow Curve, PCA Scatter Plot, Heatmaps, Cluster Profiles)
- 📖 Project Documentation (README)


## 🚀 Future Improvements

The project can be further enhanced by implementing the following improvements:

- Compare K-Means with DBSCAN and Hierarchical Clustering.
- Experiment with different dimensionality reduction techniques such as t-SNE and UMAP.
- Develop a complete Streamlit web application for interactive cluster prediction.
- Integrate the project with a music recommendation engine.
- Deploy the application on Streamlit Community Cloud.
- Build an API for real-time music clustering.


## 📚 Key Learnings

This project strengthened my understanding of:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Scaling
- Unsupervised Machine Learning
- K-Means Clustering
- Cluster Evaluation Techniques
- Principal Component Analysis (PCA)
- Business Interpretation of Machine Learning Results
- Model Serialization using Pickle
- End-to-End Machine Learning Project Development


### Author

### Mukul Chakravorty

Data Scientist specializing in Machine Learning, Data Analytics, and Artificial Intelligence. Experienced in developing end-to-end machine learning solutions, performing exploratory data analysis, feature engineering, predictive modeling, and building interactive data applications.

**Core Skills**

- Python
- SQL
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Data Visualization
- Machine Learning
- Exploratory Data Analysis (EDA)

## 📄 License

This project is developed for educational purposes and portfolio demonstration. The project may be freely used for learning, research, and personal development with appropriate attribution.


### Acknowledgements

This project was developed as part of a Machine Learning learning journey focused on building real-world data science solutions. It demonstrates the complete workflow of an unsupervised learning project, from data preprocessing and clustering to business interpretation and deployment preparation.

