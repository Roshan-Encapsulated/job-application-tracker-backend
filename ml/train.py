from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from .LoadData import get_data
import pandas as pd
import joblib

data = get_data()


X = data.drop(columns = ['success'])
Y = data['success']
x_encoded = pd.get_dummies(X, columns = ['company','role','platform'], drop_first = True)

#saving columns
columns = x_encoded.columns.tolist()


X_train, X_test, Y_train, Y_test = train_test_split(x_encoded, Y, test_size = 0.2, random_state = 42)

model = LogisticRegression()

model.fit(X_train, Y_train)
prediction = model.predict(X_test)

print(data.shape)
print(data["success"].value_counts())


joblib.dump(columns, 'models/columns.pkl')
print("columns saved")
joblib.dump(model, 'models/model.pkl')
print("model saved")
