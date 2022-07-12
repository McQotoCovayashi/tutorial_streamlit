import streamlit as st
from PIL import Image

st.title('サプーアプリ')
st.caption("これはサプーの動画用のテストアプリです")

col1, col2 = st.columns(2)

with col1:

    st.subheader('自己紹介')
    st.text("Pythonに関する情報をYoutube場で発信しているPython Vtuber サプーです\n"
    "よろしければチャンネル登録よろしくお願いいします！")

    code = '''

    import streamlit as st

    st.title('サプーアプリ')

    '''

    st.code(code, language='python')

with col2:

    #イメージ
    image = Image.open('test_image.png')
    st.image(image,width = 200)

    # movie
    # video_file = open('https://www.youtube.com/watch?v=4nsTce1Oce8')
    # video_bytes = video_file.read()
    st.video('https://www.youtube.com/watch?v=4nsTce1Oce8')

    with st.form(key='profile_form'):
        name = st.text_input('name')
        address = st.text_input('住所')
        # print(name)

        age_category = st.radio(
            '年齢層',
            ('子ども（18歳未満)','大人（18歳以上)')
        )

        hobby = st.multiselect(
            '趣味',
            ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理',)
        )

        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
        if submit_btn:
            st.text(f'ようこそ　{name}さん！{address}に書籍を送りました!')
            st.text(f'年齢層　{age_category}')
            st.text(f'趣味: {", ".join(hobby)}')
