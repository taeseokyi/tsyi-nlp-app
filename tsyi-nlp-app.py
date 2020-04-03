import streamlit as st

def main():
  """ A simple NLP App """

  st.sidebar.title("Navigation")
  goto_menu = st.sidebar.radio("Go to",
    ("Home", "기능1", "기능2"))
  if goto_menu == 'Home':
      st.title("TITLE Home")
      st.subheader("Streamlit is cool.")
  elif goto_menu == "기능1":
      st.title("기능1")
      st.markdown("https://github.com/likejazz/korean-sentence-splitter")

  elif goto_menu == "기능2":
        st.title("기능2")
        st.subheader("한국어 형태소 분석기 별 문장 분리 성능비교")
        st.markdown("한나눔이 그래도 문장 분리하는데 있어서는 가장 적합하다는 결론을 얻을 수 있다. 물론 그 절대적인 수치가 높은 것은 아니기 때문에 여러 방편을 더 고민해 봐야 할 것이다.")


if __name__ == '__main__':
  main()
