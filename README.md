
# Loan Default Prediction Project

## Overview

This project focuses on developing a robust classification model for predicting loan repayment behavior for a Non-Banking Financial Company (NBFC). The goal is to enhance risk assessment and improve the loan approval process by identifying potential loan defaulters.

## Project Background

### About the NBFC
Our partner is a trusted Non-Banking Financial Company specializing in providing:
- Quick and accessible small loans
- Flexible loan options
- Competitive interest rates
- Seamless approval process

The NBFC aims to empower financial independence and bridge the gap between traditional banking and underserved communities.

## Problem Statement

Develop a machine learning classification model to:
- Predict loan repayment behavior
- Identify potential loan defaulters and non-defaulters
- Improve risk assessment in the loan approval process

## Data Overview

### Datasets
- **Historic Data**: `train_data.xlsx`
  - Loan disbursement applications with default/non-default status
  - Coverage: Past 2+ years

- **Validation Data**: `test_data.xlsx`
  - Loan disbursement applications with default/non-default status
  - Coverage: Past 3 months

### Key Features
| Column Name | Description |
|------------|-------------|
| `customer_id` | Unique customer application identifier |
| `transaction_date` | Transaction date |
| `sub_grade` | Customer classification based on geography, income, and age |
| `term` | Total loan tenure |
| `home_ownership` | Applicant's home ownership status |
| `cibil_score` | Applicant's credit score |
| `total_no_of_acc` | Total number of bank accounts held |
| `annual_inc` | Applicant's annual income |
| `int_rate` | Interest rate charged by NBFC |
| `purpose` | Loan purpose as defined by applicant |
| `loan_amnt` | Total loan amount |
| `application_type` | Applicant type |
| `installment` | Installment amount |
| `verification_status` | Applicant verification status |
| `account_bal` | Total account balance (previous month) |
| `emp_length` | Total years of employment experience |
| `loan_status` | Loan status (1: default, 0: non-default) |

## Technical Requirements

### 1. Exploratory Data Analysis (EDA)
- Notebook: `eda.ipynb`
- Requirements:
  - Perform comprehensive data analysis
  - Add comments for each analysis/chart code block

### 2. Modeling
- Script: `model_.py`
- Requirements:
  - Prepare training pipeline
  - Create at least two different models
  - Use object-oriented, class-based approach
  - Implement key class functions:
    - `load()`: Load data
    - `preprocess()`: Preprocessing steps
    - `train()`: Training steps
    - `test()`: Testing steps with evaluation summary
    - `predict()`: Inference

### 3. Model Selection
- Notebook: `model_selection.ipynb`
- Requirements:
  - Run different prepared models
  - Showcase evaluation metrics
  - Perform hyperparameter tuning if needed
  - Provide a summary explaining the final model selection

## Additional Guidelines
- Use Python 3.7+
- Follow appropriate coding standards
- Include inline comments where necessary
- Pre-run notebooks with output cells
- Submit as `<Your Full Name>.zip`

## Important Notes
- Datasets are stochastically generated and not real company data
- Submissions must be original work
- Online research and literature review are permitted

## Getting Started

### Prerequisites
- Python 3.7+
- Required libraries (list your specific requirements)

### Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run EDA: `jupyter notebook eda.ipynb`
4. Train models: `python model_.py`
5. Select best model: `jupyter notebook model_selection.ipynb`

# Loan Default Prediction using Machine Learning
Overview
This repository contains a comprehensive analysis and modeling pipeline for predicting loan defaults for a Non-Banking Financial Company (NBFC). The goal is to enhance risk assessment and improve the loan approval process by identifying potential defaulters and non-defaulters based on historical loan data.
Problem Statement
The NBFC aims to develop a classification model that predicts loan repayment behavior. The primary objective is to identify borrowers who are likely to default on their loans, thereby improving the risk assessment process and enhancing customer satisfaction.
Data Description
Two datasets are provided:
Train Data: Contains historical loan disbursement applications and their default statuses over the past two years (train_data.xlsx).
Test Data: Contains recent loan disbursement applications and their default statuses over the last three months (test_data.xlsx).
Columns in the Dataset:
customer_id: Unique identification for each customer.
transaction_date: Date of the transaction.
sub_grade: Customer classification based on various factors.
term: Total loan tenure.
home_ownership: Status of home ownership of the applicant.
cibil_score: Credit score of applicants.
total_no_of_acc: Total number of bank accounts held by the applicant.
annual_inc: Annual income of the applicant.
int_rate: Interest rate charged by the NBFC.
purpose: Purpose for taking the loan.
loan_amnt: Total loan amount.
application_type: Type of application (Individual or Joint).
installment: Installment amount.
verification_status: Verification status of the applicant.
account_bal: Total account balance as per previous month.
emp_length: Total years of employment experience.
loan_status: Loan status (1: default, 0: non-default).

