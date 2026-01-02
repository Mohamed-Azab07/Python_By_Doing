import streamlit as st


st.title("Currency Converter: USD to EUR")

conversion = st.radio("Choose the conversion: ", ("USD to EUR", "EUR to USD"))


input_value = st.number_input("Enter the amount: ")

if conversion == "USD to EUR":
    usd = st.number_input("Enter the amount in USD: ")
    euros = usd_to_euros()

else:
    euro = st.number_input("Enter the amount in EUR: ")
    dollars = euro_to_usd()