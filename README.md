🏠 House Price Prediction System
Machine Learning Project using Flask & Tailwind CSS
📌 Project Overview
This project is a Machine Learning based House Price Prediction Web Application built using:
🐍 Python
📊 Scikit-Learn
🌐 Flask
🎨 Tailwind CSS
The system predicts house prices based on input features like area, bedrooms, bathrooms, etc.
🚀 Features
✔️ Data preprocessing
✔️ Model training using regression
✔️ Model saved using Pickle (model.pkl)
✔️ Flask backend integration
✔️ Clean UI using Tailwind CSS
✔️ Real-time prediction through web form
📂 Project Structure
Copy code

house_price_prediction/
│
├── templates/          # HTML files
├── app.py              # Flask application
├── house.csv           # Dataset
├── model.pkl           # Trained ML model
├── model_training.py   # Model training logic
├── train_model.py      # Training script
└── README.md           # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repository
Bash
Copy code
git clone https://github.com/sakshirakate11/.git
cd your-repo-name house_price_prediction
2️⃣ Create virtual environment (optional but recommended)
Bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
Bash
Copy code
pip install flask package scikit-learn
4️⃣ Run the application
Bash
Copy code
python app.py
Then open:
👉 http://127.0.0.1:5000/
🧠 Machine Learning Model
Algorithm Used: Linear Regression
Dataset: house.csv
Model saved as: model.pkl
The model is trained separately using train_model.py and loaded inside app.py.
📊 How It Works
User enters house details in the form
Data is sent to Flask backend
Model predicts price
Predicted price is displayed on the UI

🎯 Future Improvements
Add more ML algorithms (Random Forest, XGBoost)
Add model accuracy comparison
Deploy on Render / Railway / Heroku
Add user authentication
👩‍💻 Author
Sakshi Balasaheb Rakate
B.Tech – Artificial Intelligence & Machine Learning
AITRC
