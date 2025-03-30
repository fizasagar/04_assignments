import streamlit as st

# Custom CSS for Gradient Background
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #C599B6, #E6B2BA, #FAD0C4);
        background-attachment: fixed;
        color: black; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Quiz Questions
quiz_data = [
    ("Which data structure is mutable?", ["Tuple", "List", "String", "Enum"], "List"),
    ("What keyword is used for defining a function?", ["func", "define", "lambda", "def"], "def"),
    ("Which of these data structures maintains order?", ["Set", "Dictionary", "List", "Enum"], "List"),
    ("How do you check if a key exists in a dictionary?", ["dict.has_key()", "if key in dict", "dict.exists()", "check key dict"], "if key in dict"),
    ("Which statement is used for decision-making?", ["if-else", "loop", "define", "class"], "if-else"),
    ("What is the default value returned by a function if no return statement is used?", ["0", "False", "None", "Empty String"], "None"),
    ("Which data structure stores unique values only?", ["List", "Set", "Dictionary", "Tuple"], "Set"),
    ("How do you define a tuple?", ["[1,2,3]", "(1,2,3)", "{1,2,3}", "'1,2,3'"] , "(1,2,3)"),
    ("Which function is used to get user input?", ["get()", "read()", "input()", "scan()"], "input()"),
    ("Which module in Python is used for working with enumerations?", ["enum_class", "enumlib", "enum", "enumtypes"], "enum")
]

st.title("Ultimate Python Quiz 🎓📖")
st.write("Answer all questions and click Submit to see your score!")

# Store answers
user_answers = {}
for i, (question, options, _) in enumerate(quiz_data):
    user_answers[i] = st.radio(f"**Q{i+1}: {question}**", options, key=f"q{i}")

# Submit button
total_questions = len(quiz_data)
if st.button("Submit"):
    score = sum(1 for i, (_, _, correct) in enumerate(quiz_data) if user_answers[i] == correct)
    st.balloons()
    st.success(f"🎉 You scored {score} out of {total_questions}!")
    remarks = "Excellent! 🎯" if score > 8 else "Good! Keep Practicing 💡" if score > 5 else "Keep Learning! 📚"
    st.write(f"**Remarks:** {remarks}")