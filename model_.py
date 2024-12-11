# -*- coding: utf-8 -*-
"""model_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y3eHQntDp3gfV-drQ8OQ_RInwWEUnjpi
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve, confusion_matrix
import pickle
import os

class LoanDefaultModel:

    def __init__(self):
        self.models = {}
        self.model_performance = {}

    def load(self, train_path, test_path):
        """Load the datasets."""
        self.train_data = pd.read_excel(train_path)
        self.test_data = pd.read_excel(test_path)
        print("Datasets loaded successfully.")

    def preprocess(self):
        """Handle preprocessing steps."""

        self.train_data['dataset'] = 'train'
        self.test_data['dataset'] = 'test'
        data = pd.concat([self.train_data, self.test_data], axis=0)


        data.fillna(data.mean(numeric_only=True), inplace=True)
        data.fillna('Unknown', inplace=True)


        categorical_cols = data.select_dtypes(include=['object']).columns
        data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)


        for col in data.select_dtypes(include=['datetime64']).columns:
            data[col] = pd.to_numeric(data[col]) # converting datetime column to numeric values


        self.train_data = data[data['dataset_train'] == 1].drop(['dataset_train'], axis=1)
        self.test_data = data[data['dataset_train'] == 0].drop(['dataset_train'], axis=1)


        self.X_train = self.train_data.drop(['loan_status', 'customer_id'], axis=1)
        self.y_train = self.train_data['loan_status']
        self.X_test = self.test_data.drop(['loan_status', 'customer_id'], axis=1)
        self.y_test = self.test_data['loan_status']

        print("Preprocessing completed.")

    def train(self, model_type='LogisticRegression', params=None):
        """Train the models."""
        if model_type == 'LogisticRegression':
            model = LogisticRegression(max_iter=500, random_state=42)
        elif model_type == 'RandomForest':
            model = RandomForestClassifier(random_state=42)
        else:
            raise ValueError("Unsupported model type")

        #Grid Search Tuning
        if params:
            grid_search = GridSearchCV(estimator=model, param_grid=params, cv=5, scoring='accuracy', n_jobs=-1)
            grid_search.fit(self.X_train, self.y_train)
            model = grid_search.best_estimator_

        else:
            model.fit(self.X_train, self.y_train)

        self.models[model_type] = model
        print(f"{model_type} trained successfully.")

    def test(self):
        """Evaluate models on the test set."""
        for model_name, model in self.models.items():
            y_pred = model.predict(self.X_test)
            y_proba = model.predict_proba(self.X_test)[:, 1]

            acc = accuracy_score(self.y_test, y_pred)
            auc = roc_auc_score(self.y_test, y_proba)


            self.model_performance[model_name] = {
                'accuracy': acc,
                'roc_auc': auc
            }

            print(f"\nModel: {model_name}")
            print(f"Accuracy: {acc}")
            print(f"ROC-AUC: {auc}")
            print("Classification Report:")
            print(classification_report(self.y_test, y_pred))

    def save_models(self):
        """Save all trained models."""

        os.makedirs('models', exist_ok=True)


        for model_name, model in self.models.items():

            filename = f'models/{model_name.lower()}_model.pkl'


            with open(filename, 'wb') as f:
                pickle.dump(model, f)


            performance = self.model_performance.get(model_name, {})
            print(f"{model_name} model saved as {filename}")
            print(f"Model Performance - Accuracy: {performance.get('accuracy', 'N/A')}, ROC-AUC: {performance.get('roc_auc', 'N/A')}")

    def predict(self, input_data, model_type=None):
        """Make predictions using a specific model or the best performing model."""
        if model_type and model_type in self.models:
            model = self.models[model_type]
        elif len(self.models) == 1:

            model = list(self.models.values())[0]
        else:

            best_model_name = max(self.model_performance, key=lambda k: self.model_performance[k]['roc_auc'])
            model = self.models[best_model_name]

        predictions = model.predict(input_data)
        return predictions

if __name__ == '__main__':
    model = LoanDefaultModel()


    model.load(train_path='train_data.xlsx', test_path='test_data.xlsx')


    model.preprocess()


    model.train(model_type='LogisticRegression', params={'C': [0.1, 1, 10]})
    model.train(model_type='RandomForest', params={'n_estimators': [100, 200], 'max_depth': [10, 20]})


    model.test()


    model.save_models()

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PowerTransformer, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, precision_recall_curve, average_precision_score
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pickle
import os
import warnings

class EnhancedLoanDefaultModel:

    def __init__(self, random_state=42):
        self.random_state = random_state
        self.models = {}
        self.model_performance = {}
        self.preprocessor = None
        self.label_encoders = {}

    def load(self, train_path, test_path):
        """Load the datasets with enhanced error handling."""
        try:
            self.train_data = pd.read_excel(train_path)
            self.test_data = pd.read_excel(test_path)


            print("Train Data Shape:", self.train_data.shape)
            print("Test Data Shape:", self.test_data.shape)
            print("\nTrain Data Columns:", list(self.train_data.columns))
        except Exception as e:
            print(f"Error loading datasets: {e}")
            raise

    def advanced_preprocessing(self):
        """Advanced preprocessing with more sophisticated feature engineering."""

        self.train_data['dataset'] = 'train'
        self.test_data['dataset'] = 'test'
        data = pd.concat([self.train_data, self.test_data], axis=0)


        numeric_features = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_features = data.select_dtypes(include=['object']).columns.tolist()
        datetime_features = data.select_dtypes(include=['datetime64']).columns.tolist()


        columns_to_remove = ['customer_id', 'loan_status', 'dataset']
        numeric_features = [col for col in numeric_features if col not in columns_to_remove]
        categorical_features = [col for col in categorical_features if col not in columns_to_remove]


        for col in categorical_features:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col].astype(str))
            self.label_encoders[col] = le


        for col in datetime_features:
            data[f'{col}_year'] = data[col].dt.year
            data[f'{col}_month'] = data[col].dt.month
            data[f'{col}_day'] = data[col].dt.day
            numeric_features.extend([f'{col}_year', f'{col}_month', f'{col}_day'])


        preprocessor = ColumnTransformer(
            transformers=[
                ('num', Pipeline([
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler()),
                    ('power_transform', PowerTransformer(method='yeo-johnson'))
                ]), numeric_features)
            ])


        self.preprocessor = preprocessor


        X = data.drop(['loan_status', 'customer_id', 'dataset'], axis=1)
        y = data['loan_status']


        X_train = X[data['dataset'] == 'train']
        X_test = X[data['dataset'] == 'test']
        y_train = y[data['dataset'] == 'train']
        y_test = y[data['dataset'] == 'test']

        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train, model_type='advanced_ensemble', params=None):
        """Enhanced model training with more robust techniques."""

        warnings.filterwarnings('ignore')


        pipeline = Pipeline([
            ('preprocessor', self.preprocessor),
            ('feature_selection', SelectKBest(score_func=f_classif, k='all')),
            ('classifier', LogisticRegression(max_iter=1000, random_state=self.random_state))
        ])


        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=self.random_state)
        cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='roc_auc')

        pipeline.fit(X_train, y_train)
        self.models[model_type] = pipeline

        print(f"Cross-Validation ROC-AUC Scores: {cv_scores}")
        print(f"Mean CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

    def test(self, X_test, y_test):
        """Comprehensive model evaluation."""
        for model_name, model in self.models.items():

            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1]


            accuracy = accuracy_score(y_test, y_pred)
            roc_auc = roc_auc_score(y_test, y_proba)
            avg_precision = average_precision_score(y_test, y_proba)


            report = classification_report(y_test, y_pred)


            self.model_performance[model_name] = {
                'accuracy': accuracy,
                'roc_auc': roc_auc,
                'avg_precision': avg_precision,
                'classification_report': report
            }


            print(f"\n--- {model_name} Model Performance ---")
            print(f"Accuracy: {accuracy:.4f}")
            print(f"ROC-AUC: {roc_auc:.4f}")
            print(f"Average Precision Score: {avg_precision:.4f}")
            print("\nDetailed Classification Report:")
            print(report)

    def save_models(self):
        """Advanced model saving with more details."""
        os.makedirs('models', exist_ok=True)

        for model_name, model in self.models.items():
            filename = f'models/{model_name}_model.pkl'
            with open(filename, 'wb') as f:
                pickle.dump(model, f)


            perf_filename = f'models/{model_name}_performance.pkl'
            with open(perf_filename, 'wb') as f:
                pickle.dump(self.model_performance[model_name], f)

            print(f"Model {model_name} saved. Performance details saved to {perf_filename}")

    def predict(self, input_data):
        """Prediction method with the best model."""
        if not self.models:
            raise ValueError("No models have been trained.")


        model = list(self.models.values())[0]
        return model.predict(input_data)

if __name__ == '__main__':

    warnings.filterwarnings('ignore')


    model = EnhancedLoanDefaultModel()


    model.load(train_path='cleaned_train_data.xlsx', test_path='cleaned_test_data.xlsx')


    X_train, X_test, y_train, y_test = model.advanced_preprocessing()


    model.train(X_train, y_train)


    model.test(X_test, y_test)


    model.save_models()
