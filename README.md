Project Description: 
Imagine you could look into a crystal ball and see exactly how much your electricity bill would change if you ran your AC for two fewer hours today, or if the temperature outside suddenly dropped. That is exactly what this project does.
This Smart Home Daily Energy Cost Predictor is an end-to-end Machine Learning product. It takes a massive, messy dataset of over 500,000 rows of smart-meter sensor data and transforms it into a clean, interactive web app where anyone can slide buttons to predict their home’s daily power bill in real-time.

How It Works Under the Hood:
The project is split into two major halves that talk to each other seamlessly:

The Brain (The ML Engine): Built inside a Jupyter Notebook using Python and scikit-learn. It analyzes 9 different features simultaneously—including high-draw appliances (like furnaces and dishwashers) and outdoor weather conditions (temperature, humidity, cloud cover)—to find the mathematical patterns behind power costs.

The Face (The Streamlit UI): Built inside PyCharm, this is the interactive web dashboard. It loads the "frozen" brain of the model using joblib and instantly recalculates the cost estimate the exact millisecond a user drags an appliance slider.

Why This Project is Clever :
Standard machine learning models often break when users feed them weird inputs. For example, if you turn all your appliance sliders down to zero, a regular linear regression model might calculate a negative cost (meaning the electricity company owes you money just for existing!).

To fix this, I engineered a Post-Processing Safety Gate into the backend code. If the raw math skews negative, the app automatically overrides it and displays a realistic ₹50.00 base connection fee (the standard standing charge for being hooked up to the power grid). This prevents the user interface from ever displaying broken information!

Key Skills Shown in This Project :
Handling and cleaning large datasets (500K+ rows).
Deploying a machine learning model out of a sandbox notebook into a real app file.
Writing defensive code to prevent edge-case errors.

Smart_Home_Energy_Predictor/
├── app.py                         # The interactive Streamlit user interface
├── energy_regression_model.pkl    # Serialized ML engine weights & coefficients
├── model_features.pkl             # Metadata map for slider column matching
└── home_energy_predictor.ipynb    # Original Jupyter notebook with data training steps

Git and GitHub project tracking.
