**AI Guardian** is a unified, real-time intelligence platform that integrates multiple AI models to monitor and predict risks across healthcare, environment, agriculture, and defense/military. The system leverages real-time Air Quality Index (AQI) data provided by Indian Govt agencies to provide health advisories regarding air pollution, uses machine learning models to assist in early autism prediction, applies computer vision to detect wheat crop diseases, and identifies aerial threats like drones and aircraft using object detection models for military and defense applications.

By combining these domains into a single platform, AI Guardian empowers individuals, farmers, healthcare professionals, and authorities with actionable insights, enabling faster interventions, improved outcomes, and data-driven decision-making.

Target market:
Urban residents,Parents & healthcare professionals,Farmers,Militatry & surveillance agencies

Datasets used:

Air Quality Index:	https://www.data.gov.in/catalog/real-time-air-quality-index
Austism Disease Prediction:	https://www.kaggle.com/competitions/autismdiagnosis/data
Wheat Diesease Prediction:	https://www.kaggle.com/competitions/beyond-visible-spectrum-ai-for-agriculture-2026/data
Drone Military Application - Detect objects like drone, human, Ship, aircraft, etc:	https://www.kaggle.com/competitions/leonardo-airborne-object-recognition-challenge/data

# Created by

# **Team Bruhaspati Sena**

Gnanendra Sri Phani Sai Channamsetty
phanisai97@gmail.com • +91 7036389465


Perumalla Venkata Karthik
kperumalla98@gmail.com • +91 9398885899


# We got stuck at these points and we resolved them:

02AutismDataset:
Featue engineering - Few columns like a ethnicity and relation were corrupted. Had doubt on which columns to remove, which columns should we consider for training model. Ultimately created 3 datasets from the original dataset, 1 after removing null value and imputing with median or mode, second after scaling, third after PCA.
Next problem was model selection. As intially doing DT model, Gradient_Boosting model, SVM model were not satisfactory.
So created 8 models using 4 fold cross validation and ultiamtely selected the model which peformed best on test dataset.
models = {
    "Logistic_Regression": LogisticRegression(max_iter=1000),
    "SVM_SVC": SVC(probability=True),
    "Random_Forest": RandomForestClassifier(random_state=42),
    "Gradient_Boosting": GradientBoostingClassifier(random_state=42),
    "AdaBoost": AdaBoostClassifier(random_state=42),
    "Extra_Trees": ExtraTreesClassifier(random_state=42),
    "Decision_Tree": DecisionTreeClassifier(random_state=42),
    "K_Neighbors": KNeighborsClassifier(),
    "LightGBM": LGBMClassifier(random_state=42, verbose=-1)
}