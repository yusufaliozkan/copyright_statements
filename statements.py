import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import pandas as pd
import pyperclip

st.set_page_config(layout = "wide", page_title='Imperial College London - Spiral non-compliant submissions statistics dashboard')
path='https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Logo_for_Imperial_College_London.svg/2560px-Logo_for_Imperial_College_London.svg.png'
image = path
st.image(image, width=300)

df = pd.read_excel(r'statements.xlsx', sheet_name='Sheet1')
df['publisher'] = df['publisher'].astype(str)

df_new=df.sort_values(by='publisher')

# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language='python')

st.markdown("# Copyright statements dashboard")
st.sidebar.markdown("# Copyright statements dashboard")

col1,col2 = st.columns(2)

clist = df_new['publisher'].unique()
publisher = st.selectbox("Select a publisher:",clist)
col1, col2 = st.columns(2)

df_statement = df.loc[df_new['publisher']==publisher, 'statement'].values[0]
df_statement

text_to_be_copied = df_statement
copy_dict = {"content": text_to_be_copied}

copy_button = Button(label="Copy Text")
copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
    navigator.clipboard.writeText(content);
    """))

no_event = streamlit_bokeh_events(
    copy_button,
    events="GET_TEXT",
    key="get_text",
    refresh_on_update=True,
    override_height=75,
    debounce_time=0)

with st.expander("See all publisher statements"):
    df_new
    copy_button = Button(label="Copy data all copyright statements")
    copy_button.js_on_event("button_click", CustomJS(args=dict(df_new=df_new.to_csv(sep='\t')), code="""
        navigator.clipboard.writeText(df_new);
        """))

    no_event = streamlit_bokeh_events(
        copy_button,
        events="GET_TEXT2",
        key="get_text2",
        refresh_on_update=True,
        override_height=75,
        debounce_time=0)        
