import streamlit as st
import pandas as pd

st.title("📊 Student Result Analyzer")

name = st.text_input("Student Name")

maths = st.number_input("Maths Marks", 0, 100)
science = st.number_input("Science Marks", 0, 100)
english = st.number_input("English Marks", 0, 100)

if "results" not in st.session_state:
    st.session_state.results = []

if st.button("Analyze Result"):
    total = maths + science + english
    percentage = total / 3

    # Grade logic
    if percentage >= 90:
        grade = "A+"
        stars = "⭐⭐⭐⭐⭐"
    elif percentage >= 75:
        grade = "A"
        stars = "⭐⭐⭐⭐"
    elif percentage >= 60:
        grade = "B"
        stars = "⭐⭐⭐"
    elif percentage >= 40:
        grade = "C"
        stars = "⭐⭐"
    else:
        grade = "Fail"
        stars = "⭐"

    st.session_state.results.append({
        "Name": name,
        "Maths": maths,
        "Science": science,
        "English": english,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade,
        "Stars": stars
    })

    st.success("Result analyzed successfully 🎉")

# Show results
if st.session_state.results:
    df = pd.DataFrame(st.session_state.results)

    st.subheader("📋 Student Results")
    st.dataframe(df)

    st.subheader("📈 Percentage Chart")
    st.bar_chart(df.set_index("Name")["Percentage"])

