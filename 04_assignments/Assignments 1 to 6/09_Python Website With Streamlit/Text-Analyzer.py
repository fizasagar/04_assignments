import streamlit as st
import re

def main():
    st.set_page_config(page_title="Text Analyzer", page_icon="🔍", layout="centered")

    st.markdown("""
        <style>
            .stApp { background-color: #ebecda; }
            .stTextArea, .stTextInput { border-radius: 10px; }
            .stButton>button { background: blue; color: white; border-radius: 10px; padding: 10px; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🔍 Text Analyzer in Python")
    st.write("Transform, analyze, and enhance your text instantly! 🚀")

    paragraph = st.text_area("📝 Enter a paragraph:", "", height=150)

    if paragraph:
        st.markdown("---")
        st.subheader("📊 Analysis Results")

        words = paragraph.split()
        word_count = len(words)
        char_count = len(paragraph)

        col1, col2 = st.columns(2)
        col1.metric("📝 Total Words", word_count)
        col2.metric("🔢 Total Characters", char_count)

        # Search and replace feature
        st.subheader("🔄 Search and Replace")
        search_word = st.text_input("🔍 Enter a word to search:")
        replace_word = st.text_input("✏️ Enter a word to replace with:")

        if search_word and replace_word:
            modified_paragraph = re.sub(rf'\b{re.escape(search_word)}\b', replace_word, paragraph)
            st.success("✅ Modified Paragraph:")
            st.info(modified_paragraph)

        # Uppercase and Lowercase feature
        st.subheader("Uppercase and Lowercase")
        st.write("**🔠 UPPERCASE:**")
        st.text(paragraph.upper())
        st.write("**🔡 Lowercase:**")
        st.text(paragraph.lower())

        # Check if "Python" exists
        contains_python = "✅ Yes" if "Python" in paragraph else "❌ No"
        st.write(f"Contains 'Python': {contains_python}")

        # Average word length
        average_word_length = char_count / word_count if word_count else 0
        st.write(f"📏 Average Word Length: {average_word_length:.2f}")

    else:
        st.warning("⚠️ Please enter a paragraph for analysis.")

if __name__ == "__main__":
    main()
