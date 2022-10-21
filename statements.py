import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import pandas as pd
import pyperclip

st.set_page_config(layout = "wide", page_title='Copyright statements dashboard', page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Copyright.svg/220px-Copyright.svg.png")
path='https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Logo_for_Imperial_College_London.svg/2560px-Logo_for_Imperial_College_London.svg.png'
path2 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Copyright.svg/220px-Copyright.svg.png'
st.image(path2, width=75)

# df = pd.read_excel(r'statements.xlsx', sheet_name='Sheet1')
df = pd.read_csv(r'statements.csv')
df['publisher'] = df['publisher'].astype(str)

df_new=df.sort_values(by='publisher')

st.markdown("# Copyright statements dashboard")
st.write('This page shows set copyright statements that need to accompany self-archiving in institutional repositories. From the dropdown menu, select the publisher and then copy the statement to clipboard.')

st.sidebar.image(path2, width=150)
st.sidebar.markdown("# Copyright statements dashboard")

clist = df_new['publisher'].unique()
publisher = st.selectbox("Select a publisher:",clist)

df_statement = df.loc[df_new['publisher']==publisher, 'statement'].values[0]
df_statement

if st.button('Copy to clipboard'):
    c.copy(df_statement)

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

#Frequently used statements
with st.expander("Frequently used copyright statements"):
    st.write('Publisher statements. Click on the button to copy the statement.')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        text_to_be_copied = df.loc[df_new['publisher']=='Elsevier', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="Elsevier")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXT3",
            key="get_text3",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)

    with col2:
        text_to_be_copied = df.loc[df_new['publisher']=='Wiley', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="Wiley")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXT4",
            key="get_text4",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)

    with col3:
        text_to_be_copied = df.loc[df_new['publisher']=='Springer Nature', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="Springer Nature")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXT5",
            key="get_text5",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)

    with col4:
        text_to_be_copied = df.loc[df_new['publisher']=='IEEE ', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="IEEE")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXT6",
            key="get_text6",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        text_to_be_copied = df.loc[df_new['publisher']=='SAGE publications', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="SAGE publications")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXT7",
            key="get_text7",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)
    with col2:
        text_to_be_copied = df.loc[df_new['publisher']=='BMJ Publishing', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="BMJ Publishing")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXT8",
            key="get_text8",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)

    with col3:
        text_to_be_copied = df.loc[df_new['publisher']=='Oxford University Press (OUP)', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="Oxford University Press (OUP)")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXT9",
            key="get_text9",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)

    with col4:
        text_to_be_copied = df.loc[df_new['publisher']=='American Chemical Society', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="American Chemical Society")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXT10",
            key="get_text10",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)
        
    st.write('Creative Commons statements. Click on the button to copy the statement.')

    col1, col2, col3 = st.columns(3)

    with col1:
        text_to_be_copied = df.loc[df_new['publisher']=='CC BY licence', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="CC BY")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXTccby",
            key="get_textccby",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)

    with col2:
        text_to_be_copied = df.loc[df_new['publisher']=='CC BY-NC licence', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="CC BY-NC")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXTccbync",
            key="get_textccbync",
            refresh_on_update=True,
            override_height=75,
            debounce_time=0)
    
    with col3:
        text_to_be_copied = df.loc[df_new['publisher']=='CC BY-NC-ND licence', 'statement'].values[0]
        copy_dict = {"content": text_to_be_copied}

        copy_button = Button(label="CC BY-NC-ND")
        copy_button.js_on_event("button_click", CustomJS(args=copy_dict, code="""
            navigator.clipboard.writeText(content);
            """))

        no_event = streamlit_bokeh_events(
            copy_button,
            events="GET_TEXTccbyncnd",
            key="get_textccbyncnd",
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
        events="GET_TEXT11",
        key="get_text11",
        refresh_on_update=True,
        override_height=75,
        debounce_time=0)


    # if st.button('Copy all statements to clipboard'):
    #     pyperclip.copy(df_new.to_csv(sep='\t'))
    # else:
    #     st.write('')
    
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df_new)

    st.download_button("Press to Download", csv, "copyright_statements.csv", "text/csv", key='download-csv')


with st.expander("About the dashboard"):
    st.write('This app was launched in October 2022.')
    st.write('Source code of this app is available\n [here](https://github.com/YusufAliOzkan/copyright_statements).')
    st.write("**Get in touch!**")   
    contact_form = """
    <form action="https://formsubmit.co/yusufaliozkan37@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style.css")
    

