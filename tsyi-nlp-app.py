import streamlit as st

def main():
  """ A simple NLP App """
  st.title("TITLE")
  st.subheader("Streamlit is cool.")
  st.sidebar.title("Navigation")
  goto_menu = st.sidebar.radio("Go to",
    ("Home", "기능1", "기능2"))
  if goto_menu == 'Home':
      st.title("TITLE Home")
      st.subheader("Streamlit is cool.")
  elif goto_menu == "기능1":
      st.title("기능1")
      st.subheader("Streamlit is cool.")

if __name__ == '__main__':
  main()
