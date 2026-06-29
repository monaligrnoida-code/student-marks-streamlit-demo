import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Marks Analyzer", page_icon="📊", layout="centered"
)

st.title("Student Marks Analyzer")
st.write("Enter your marks and analyze your performance.")

# Input section
name = st.text_input("Student name", "Hello")

maths = st.number_input("Maths", min_value=0, max_value=100, value=85)
physics = st.number_input("Physics", min_value=0, max_value=100, value=80)
chemistry = st.number_input("Chemistry", min_value=0, max_value=100, value=75)
computer_science = st.number_input(
    "Computer Science", min_value=0, max_value=100, value=90
)
english = st.number_input("English", min_value=0, max_value=100, value=88)

subjects = {
    "Maths": maths,
    "Physics": physics,
    "Chemistry": chemistry,
    "Computer Science": computer_science,
    "English": english,
}

total = sum(subjects.values())
percentage = total / len(subjects)

# Grade logic
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Output section
st.subheader("Result Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Marks", f"{total}/500")
col2.metric("Percentage", f"{percentage:.2f}%")
col3.metric("Grade", grade)

st.write(f"### Performance report for {name}")

df = pd.DataFrame({"Subject": list(subjects.keys()), "Marks": list(subjects.values())})

st.dataframe(df, use_container_width=True)

st.bar_chart(df.set_index("Subject"))

# Feedback
st.subheader("Feedback")

if percentage >= 90:
    st.success("Excellent performance. Keep maintaining consistency.")
elif percentage >= 75:
    st.info("Good performance. Focus on weaker subjects to reach 90%+.")
elif percentage >= 50:
    st.warning("Average performance. Create a revision plan and solve more problems.")
else:
    st.error("Needs serious improvement. Start with fundamentals and daily practice.")
