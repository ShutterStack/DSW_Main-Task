# DSW_Main-Task
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
