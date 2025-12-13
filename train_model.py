import pandas as pd
from sklearn.model_selection import train_test_split

# load dataset
df = pd.read_csv("house.csv")
print(df.columns)
print(df.info())

# Select input features (X) and target (y)
X = df[['area', 'bedrooms', 'bathrooms', 'parking']]
y = df['price']

print(X.head())
print(y.head())

#Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data size:", X_train.shape)
print("Testing data size:", X_test.shape)


# Step 5: Select features and target
X = df[['area', 'bedrooms', 'bathrooms', 'parking']]
y = df['price']

print(X.head())
print(y.head())

# show first 5 rows
print(df.head())

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

print("Model training completed successfully")

# Step : Evaluate the model
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)
print("Model Accuracy (R2 score):", accuracy)

import pickle

# Save the trained model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved as model.pkl")


