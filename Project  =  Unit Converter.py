# Unit Converter Project :

import streamlit as st
import random

def convert_units(value : float , unit_from : str , unit_to : str) :

    if unit_from == "kilometers" and unit_to == "meters" :
        return value * 1000
    
    elif unit_from == "meters" and unit_to == "kilometers" :
        return value * 0.001
    
    elif unit_from == "kilograms" and unit_to == "grams" :
        return value * 1000
    
    elif unit_from == "grams" and unit_to == "kilograms" :
        return value * 0.001
    
    else :
        return "Conversion is not supported!"
        

result1 = convert_units(1.5 , "kilometers" , "meters")
print("result value in meter is = " , result1)

result2 = convert_units(5000 , "grams" , "kilograms")
print("result value in kilograms is = " , result2)

def main() :
    st.title("Unit Converter")
    st.header("Welcome To Unit Converter !")

    value = st.number_input("Enter the value you want to convert :" , min_value = 0.0)
    unit_from = st.text_input("Enter the unit you want to convert from e.g. meters , kilometers , grams , kilograms : ")
    unit_to = st.text_input("Enter the unit you want to conversion from e.g. meters , kilometers , grams , kilograms : ")

    if st.button("Convert"):
        result = convert_units(value , unit_from , unit_to)
        st.write("Converted value is = " , result)

main()    

# << practiced by Bint e Zain >>