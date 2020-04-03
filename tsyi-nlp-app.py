import streamlit as st

def main():
  """ A simple NLP App """

  st.sidebar.title("Navigation")
  goto_menu = st.sidebar.radio("Go to",
    ("Home", "기능1", "기능2"))
  st.sidebar.title("About")
  st.sidebar.info('''
- 우리는 자연 언어 생성에서 최첨단 기술을 발전시켜 연구자에게 새로운 기회를 제공합니다.

- 우리는 문서를 요약하여 사용자 시간을 절약하는 것 외에도 논문 작성을 지원하거나 연구관련 질문에 답변함으로써 KISTI 서비스에 대한 경험을 향상시킬 수 있습니다.

- 또한 자연어 문장 생성 기술은 연구자와 대화하는 유창한 챗봇과 디지털 어시스턴트를 위한 길을 닦을 수 있습니다.

- 우리는 언어 모델의 질을 계속 향상시키면서 새로운 가능성을 탐색합니다.

[KISTI 융합서비스 센터]
  '''
  )
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
