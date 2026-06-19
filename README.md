Smart Home Daily Energy Cost Predictor :
Imagine you could look into a crystal ball and see exactly how much your electricity bill would change if you ran your AC for two fewer hours today, or if the temperature outside suddenly dropped. That is exactly what this project does.
This Smart Home Daily Energy Cost Predictor is an end-to-end Machine Learning product. It takes a massive, messy dataset of over 500,000 rows of smart-meter sensor data and transforms it into a clean, interactive web app where anyone can manipulate sliders to predict their home’s daily power bill in real-time.

Live link : https://smarthomeenergypredictor-vgje9gfdexu9jy6uezfpen.streamlit.app/

 How It Works Under the Hood : 
The project is split into two major halves that communicate with each other seamlessly:

The Brain (The ML Engine): Built inside a Jupyter Notebook using Python and scikit-learn. It analyzes 9 different features simultaneously—including high-draw appliances (like heating furnaces and dishwashers) and outdoor weather conditions (temperature, humidity, cloud cover)—to unlock the mathematical patterns behind power costs.

The Face (The Streamlit UI): Built natively inside PyCharm, this is your interactive web dashboard interface. It loads the "frozen" brain of the model using joblib and instantly recalculates cost estimates the exact millisecond a user drags an appliance slider.

Why This Project is Clever :
Standard machine learning models often break when users feed them edge-case inputs. For example, if you turn all your appliance operational sliders down to zero, a regular linear regression model might calculate a negative cost (theoretically implying the utility company owes you money just for existing!).

To resolve this limitation, I engineered a Post-Processing Safety Gate into the backend application logic. If the raw mathematical equation skews negative, the app automatically intercepts the value and overrides it to display a realistic ₹50.00 base connection fee (representing the standard standing service charge for remaining hooked up to the power grid). This defensive programming approach prevents the user interface from ever displaying broken or illogical data.

Key Skills Demonstrated :
Large-Scale Data Engineering: Handling, parsing, and cleaning massive time-series datasets containing over 500K+ rows of raw smart-meter sensor entries.

Model Operationalization: Successfully deploying a machine learning model out of an isolated training sandbox (Jupyter Notebook) directly into a portable, production-ready app service script.

Defensive Software Engineering: Designing logic gates to catch boundary skews and safeguard customer-facing presentation tiers against algorithmic edge-case exceptions.
