import streamlit as st
import joblib
import pandas as pd

# Load the trained model and encoded mappings
model = joblib.load('land_price_prediction_model.pkl')
encoding = joblib.load('encoded_mappings.pkl')

df = pd.read_csv('processed_data.csv')

cat_cols = ['AREA', 'SALE_COND', 'PARK_FACIL', 'BUILDTYPE', 'UTILITY_AVAIL', 'STREET', 'MZZONE']
unique_values = {col: df[col].unique().tolist() for col in cat_cols}

# Set page configuration
st.set_page_config(
    page_title="Chennai Land Price Prediction",
    page_icon="🏞️",
    layout="wide",
)

# Add custom CSS to style widgets and buttons
st.markdown(
    """
    <style>
    .stSelectbox, .stNumberInput {
        border: 2px solid #8B4513 !important;
        border-radius: 5px !important;
        padding: 10px !important;
        background-color: #F5F5DC !important;
        color: #8B4513 !important;
    }
    .stButton > button {
        background-color: #8B4513 !important;
        color: white !important;
        border-radius: 5px !important;
        padding: 10px 20px !important;
    }
    .custom-container {
        background-color: #F5F5DC;
        border: 3px solid #8B4513;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    .custom-title {
        color: #8B4513;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
    }
    .custom-point {
        color: #8B4513;
        font-size: 18px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a sidebar for navigation
st.sidebar.title("Chennai Land Price Prediction")
st.sidebar.image(
    "land_price_predict_logo.jpg", caption="Unlock the future of real estate with data-driven insights—predict Chennai's land prices, one plot at a time.", use_container_width=True
)

# Main page content
st.markdown(
    """
    <div class="custom-container">
        <h1 class="custom-title">Chennai Land Price Prediction 🏞️</h1>
        <ul>
            <li class="custom-point">Leverage historical and current market trends to provide accurate Chennai land price predictions.</li>
            <li class="custom-point">Utilize geospatial mapping to offer price variations across different areas in Chennai.</li>
            <li class="custom-point">Incorporate ML algorithms to predict future land price trends based on economic and urban development factors.</li>
            <li class="custom-point">Allow users to filter predictions based on location, plot size, zoning, and proximity to amenities.</li>
            <li class="custom-point">Notify users of significant changes in land prices or upcoming real estate opportunities in Chennai.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Reset functionality
if "reset" not in st.session_state:
    st.session_state.reset = False

# Reset values logic
def reset_values():
    st.session_state.area = "---- Select the area name ---"
    st.session_state.squarefeet = 0
    st.session_state.mainroaddistance = 0
    st.session_state.bedroomcount = 0
    st.session_state.bathroomcount = 0
    st.session_state.roomcount = 0
    st.session_state.salecondition = "---- Select the sale condition ---"
    st.session_state.parkingfacility = "---- Select the parking facility ---"
    st.session_state.builttype = "---- Select the build type ---"
    st.session_state.utilityavailable = "---- Select utility availability ---"
    st.session_state.street = "---- Select the street type ---"
    st.session_state.mzzone = "---- Select the Mz Zone ---"
    st.session_state.roomrating = 0.0
    st.session_state.bathroomrating = 0.0
    st.session_state.bedroomrating = 0.0
    st.session_state.overallrating = 0.0
    st.session_state.regfees = 0
    st.session_state.commision = 0
    st.session_state.ageofbuilding = 0

if st.session_state.reset:
    reset_values()
    st.session_state.reset = False

# Create a form layout for user inputs
with st.form("Chennai Land Price Prediction Form"):
    st.subheader("Enter Details Here")
    
    # Create two columns for aligning widgets
    col1, col2 = st.columns(2)
    
    # Widgets in the first column
    with col1:
        area = st.selectbox("Area", ["---- Select the area name ---"] + unique_values['AREA'], key="area")
        square_feet = st.number_input("Area Square Feet", min_value=int(df['INT_SQFT'].min()), max_value=int(df['INT_SQFT'].max()), step=100, key="squarefeet")
        distance_mainroad = st.number_input("Distance From Mainroad", min_value=int(df['DIST_MAINROAD'].min()), max_value=int(df['DIST_MAINROAD'].max()), step=10, key="mainroaddistance")
        bedroom_count = st.number_input("No Of Bedrooms", min_value=int(df['N_BEDROOM'].min()), max_value=10, step=1, key="bedroomcount")
        bathroom_count = st.number_input("No Of Bathrooms", min_value=int(df['N_BATHROOM'].min()), max_value=10, step=1, key="bathroomcount")
        room_count = st.number_input("No Of Rooms", min_value=int(df['N_ROOM'].min()), max_value=20, step=1, key="roomcount")
        sale_condition = st.selectbox("Sales Condition", ["---- Select the sale condition ---"] + unique_values['SALE_COND'], key="salecondition")
        parking_facility = st.selectbox("Parking Facility", ["---- Select the parking facility ---"] + unique_values['PARK_FACIL'], key="parkingfacility")
        build_type = st.selectbox("Build Type", ["---- Select the build type ---"] + unique_values['BUILDTYPE'], key="builttype")
    
    # Widgets in the second column
    with col2:
        utility_available = st.selectbox("Utility Available", ["---- Select utility availability ---"] + unique_values['UTILITY_AVAIL'], key="utilityavailable")
        street = st.selectbox("Street", ["---- Select the street type ---"] + unique_values['STREET'], key="street")
        mz_zone = st.selectbox("Mz Zone", ["---- Select the Mz Zone ---"] + unique_values['MZZONE'], key="mzzone")
        bedroom_rating = st.number_input("Bedroom Rating", min_value=float(df['QS_BEDROOM'].min()), max_value=5.0, step=0.1, key="bedroomrating")
        bathroom_rating = st.number_input("Bathroom Rating", min_value=float(df['QS_BATHROOM'].min()), max_value=5.0, step=0.1, key="bathroomrating")
        room_rating = st.number_input("Room Rating", min_value=float(df['QS_ROOMS'].min()), max_value=5.0, step=0.1, key="roomrating")
        overall_rating = st.number_input("Overall Rating", min_value=float(df['QS_OVERALL'].min()), max_value=5.0, step=0.1, key="overallrating")
        reg_fees = st.number_input("Registration Fees", min_value=int(df['REG_FEE'].min()), max_value=int(df['REG_FEE'].max()), step=100, key="regfees")
        commision = st.number_input("Commision", min_value=int(df['COMMIS'].min()), max_value=1000000, step=100, key="commision")
    
    # Age of building
    age_of_building = st.number_input("Age Of Building", min_value=int(df['AGE_OF_BUILDING'].min()), max_value=int(df['AGE_OF_BUILDING'].max()), step=1, key="ageofbuilding")

    input_data = pd.DataFrame({
        'AREA': [encoding['AREA'].get(area)] if area != "---- Select the area name ---" else [None],
        'INT_SQFT': [square_feet],
        'DIST_MAINROAD': [distance_mainroad],
        'N_BEDROOM': [bedroom_count],
        'N_BATHROOM': [bathroom_count],
        'N_ROOM': [room_count],
        'SALE_COND': [encoding['SALE_COND'].get(sale_condition)] if sale_condition != "---- Select the sale condition ---" else [None],
        'PARK_FACIL': [encoding['PARK_FACIL'].get(parking_facility)] if parking_facility != "---- Select the parking facility ---" else [None],
        'BUILDTYPE': [encoding['BUILDTYPE'].get(build_type)] if build_type != "---- Select the build type ---" else [None],
        'UTILITY_AVAIL': [encoding['UTILITY_AVAIL'].get(utility_available)] if utility_available != "---- Select utility availability ---" else [None],
        'STREET': [encoding['STREET'].get(street)] if street != "---- Select the street type ---" else [None],
        'MZZONE': [encoding['MZZONE'].get(mz_zone)] if mz_zone != "---- Select the Mz Zone ---" else [None],
        'QS_ROOMS': [room_rating],
        'QS_BATHROOM': [bathroom_rating],
        'QS_BEDROOM': [bedroom_rating],
        'QS_OVERALL': [overall_rating],
        'REG_FEE': [reg_fees],
        'COMMIS': [commision],
        'AGE_OF_BUILDING': [age_of_building],
    })

    # Buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        predict_button = st.form_submit_button("Predict")
    with col2:
        reset_button = st.form_submit_button("Reset")

# Handle reset button
if reset_button:
    st.session_state.reset = True

# Handle predict button
if predict_button:
    if (
        area == "---- Select the area name ---" or
        sale_condition == "---- Select the sale condition ---" or
        parking_facility == "---- Select the parking facility ---" or
        build_type == "---- Select the build type ---" or
        utility_available == "---- Select utility availability ---" or
        street == "---- Select the street type ---" or
        mz_zone == "---- Select the Mz Zone ---"
    ):
        st.error("Please enter valid inputs for all fields.")
    else:
        prediction = model.predict(input_data.dropna(axis=1))
        st.success(f"Predicted Land Price: ₹{prediction[0]:,.2f}")
