import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import pandas as pd
import pyperclip

st.set_page_config(layout = "wide", page_title='Copyright statements dashboard')
path='https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Logo_for_Imperial_College_London.svg/2560px-Logo_for_Imperial_College_London.svg.png'
image = path
st.image(image, width=300)

# df = pd.read_excel(r'statements.xlsx', sheet_name='Sheet1')
df = pd.read_csv(r'statements.csv')
df['publisher'] = df['publisher'].astype(str)

df_new=df.sort_values(by='publisher')

st.write('This page shows set copyright statements that need to accompany self-archiving in institutional repositories. From the dropdown menu, select the publisher and then copy the statement to clipboard.')

st.markdown("# Copyright statements dashboard")
st.sidebar.markdown("# Copyright statements dashboard")

clist = df_new['publisher'].unique()
publisher = st.selectbox("Select a publisher:",clist)

df_statement = df.loc[df_new['publisher']==publisher, 'statement'].values[0]
df_statement

text_to_be_copied = df_statement
copy_dict = {"content": text_to_be_copied}

copy_button = Button(label="Copy to clipboard")
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
    
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df_new)

    st.download_button("Press to Download", csv, "copyright_statements.csv", "text/csv", key='download-csv')
    
with st.expander("More information:"):
    st.write('Source code of this app is available [here](https://github.com/YusufAliOzkan/copyright_statements).')

