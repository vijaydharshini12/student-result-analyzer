import streamlit as st
import pandas as pd

st.title("📊 Student Result Analyzer")

st.write("Enter student marks to analyze results")

# Input fields
name = st.text_input("Student Name")

maths = st.number_input("Maths Marks", 0, 100)
science = st.number_input("Science Marks", 0, 100)
english = st.number_input("English Marks", 0, 100)

if "data" not in st.session_state:
    st.session_state.data = []

# Button
if st.button("Add Result"):
    total = maths + science + english
    percentage = total / 3

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    st.session_state.data.append({
        "Name": name,
        "Maths": maths,
        "Science": science,
        "English": english,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    })

    st.success("Result added successfully!")

# Display results
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)

    st.subheader("📋 Student Results")
    st.dataframe(df)

    st.subheader("📈 Percentage Chart")
    st.bar_chart(df.set_index("Name")["Percentage"])
