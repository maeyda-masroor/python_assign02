import streamlit as st

# First Row (Full width)

st.markdown("""
    <style>
        /* Styling the select box */
        div[data-baseweb="select"] {
            background-color: #f0f0f5 !important;
            color:white;
            border: 2px solid #4CAF50 !important;
            border-radius: 8px !important;
            padding: 5px !important;
        }

        /* Styling the dropdown options */
        div[data-baseweb="popover"] {
            background-color: #ffffff !important;
            border: 2px solid #4CAF50 !important;
            border-radius: 8px !important;
            color:white;
        }

        /* Styling the text inside the select box */
        div[data-baseweb="select"] > div {
            font-size: 16px !important;
            color: white !important;

        }

        /* Hover effect */
        div[data-baseweb="select"]:hover {
            border-color: #ff9800 !important;
        }
        .custom-text-input input {
        	border: 2px solid white;
        	border-radius: 10px;
        	padding: 10px;
        	font-size: 16px;
        	color: #333;
        	background-color: white;
        	width: 100%;
    	}
    </style>
""", unsafe_allow_html=True)


conversion_factors = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": "celsius",
        "Fahrenheit": "fahrenheit",
        "Kelvin": "kelvin"
    }
}

# Conversion functions
def convert_units(value, from_unit, to_unit, conversion_type):
    if conversion_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # If same unit, return same value
    else:
        return value * (conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit])

conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))

units = list(conversion_factors[conversion_type].keys())

# Second Row (3 Columns)
col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("Enter value", min_value=0.0, step=0.1)
    from_unit = st.selectbox("Convert from", units)

# Second Column (Middle - Single Row)
with col2:
	st.markdown(
    """
    <style>
    .equal-sign {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px; /* Adjust height as needed */
        font-size: 50px; /* Increase font size */
        font-weight: bold;
        background-color: black;
        border-radius: 10px;
        border: 2px solid #333;
        margin: 20px 0;
    }
    </style>
    
    <div class="equal-sign">=</div>
    """,
    unsafe_allow_html=True,
)
# Third Column (2 Rows)
with col3:
    to_unit = st.selectbox("Convert to", units)
    result = convert_units(value, from_unit, to_unit, conversion_type)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")  # Fixed indentation

# Third Row (2 Columns)

col6,col7 = st.columns(2)
with col6:
    st.markdown(
    	f"""
    <p><span style = "background-color:yellow ; color:black">Formula</span>&nbsp; &nbsp;multiply the length value by {result:.2f}</p>
""", unsafe_allow_html=True)

