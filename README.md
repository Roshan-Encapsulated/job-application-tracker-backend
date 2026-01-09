# Job Application Tracker – ML Prediction Feature

This branch introduces **Machine Learning integration** into the backend to
predict the likelihood of a job application being successful.

## ML Objective

Predict whether a job application is likely to result in:
- Interview / Offer (Success)
- Rejection (Failure)

## Data Source

- Historical job applications stored in PostgreSQL
- Only applications with final outcomes are used for training

## Features Used

- Company
- Role
- Platform (LinkedIn, Referral, etc.)
- Candidate experience (in years)
- Day of application (derived from timestamp)

## Model Details

- Algorithm: Logistic Regression
- Library: scikit-learn
- Categorical features encoded using one-hot encoding
- Model trained offline using Pandas
- Feature schema stored to ensure correct prediction alignment

## Training Strategy

- Offline batch training
- Model retrained periodically as more labeled data is collected
- Training is not triggered during API requests

## Prediction Endpoint
### Sample Request
```json
{
  "company": "Google",
  "role": "Backend Engineer",
  "platform": "LinkedIn",
  "experience": 2.0,
  "applied_day": 2
}
```
### Sample Response
```json
{
  "success_probability": 0.42,
  "interpretation": "Low chance"
}
```
