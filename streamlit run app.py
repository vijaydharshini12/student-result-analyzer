# Import required libraries
import streamlit as st
import pandas as pd

# App title
st.title("🎓 Student Result Analyzer")

# ----------- INPUT SECTION -----------

# Input field to enter student name
name = st.text_input("Student Name")

# Input fields for marks (range: 0 to 100)
maths = st.number_input("Maths Marks", 0, 100)
science = st.number_input("Science Marks", 0, 100)
english = st.number_input("English Marks", 0, 100)

# ----------- SESSION STATE -----------

# Check if 'results' list exists in session_state
# If not, create an empty list to store student results
if "results" not in st.session_state:
    st.session_state.results = []

# ----------- RESULT ANALYSIS -----------

# Button to analyze and store result
if st.button("Analyze Result"):

    # Calculate total marks
    total = maths + science + english

    # Calculate percentage
    percentage = total / 3

    # Decide grade and stars based on percentage
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

    # Store student result as a dictionary in session_state
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

    # Success message
    st.success("Result added successfully ✅")

# ----------- DISPLAY SECTION -----------

# Check if results are available
if st.session_state.results:

    # Convert results list into a DataFrame
    df = pd.DataFrame(st.session_state.results)

    # Display results table
    st.subheader("📋 Student Results Table")
    st.dataframe(df)

    # Bar chart showing percentage of each student
    st.subheader("📊 Percentage Bar Chart")
    st.bar_chart(
        df.set_index("Name")[["Percentage"]]
    )

    # Show subject-wise marks for the last entered student
    st.subheader("📊 Subject-wise Marks (Last Student)")
    last = df.iloc[-1]

    # Create DataFrame for subject marks
    subject_df = pd.DataFrame({
        "Marks": [last["Maths"], last["Science"], last["English"]]
    }, index=["Maths", "Science", "English"])

    # Display bar chart
    st.bar_chart(subject_df)
