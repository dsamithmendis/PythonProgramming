# Step 1: Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Step 2: Load training data
train_data = pd.read_csv("student_marks_train.csv")
X_train = train_data[['maths','sinhala','english','history']]
y_train = train_data['class-label']

# Encode target labels to numbers
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)  # pass=0, maybe=1, fail=2

# Step 3: Train Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train_encoded)

# Step 4: Load test data
test_data = pd.read_csv("student_marks_test.csv")
X_test = test_data[['maths','sinhala','english','history']]

# Step 5: Predict class labels
y_test_pred = clf.predict(X_test)

# Convert numeric labels back to original class labels
y_test_labels = le.inverse_transform(y_test_pred)

# Step 6: Add predictions to test data
test_data['Predicted'] = y_test_labels

# Step 7: Print predictions
print(test_data)

# Optional: save predictions to CSV
test_data.to_csv("predictions.csv", index=False)
