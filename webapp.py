from vega_datasets import data
import streamlit as st
import altair as alt
import sqlitemanagement as db
import contragents
import pandas as pd

def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration", "About", "Images", "Invoices"])

    if page == "Homepage":
        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        st.write(df)
        
    elif page == "Exploration":
        st.title("Data Exploration")
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
        visualize_data(df, x_axis, y_axis)
    elif page == "About":
        st.title("About")
        st.write("Kaccounting is a free online invoicing & accounting tool aimed at entrepreneurs\
             and small businesses. Easily send invoices, track your hours, register your receipts\
             and track your worktrips. Kaccounting helps you to make this as simple as possible.\
             Whether you prefer to work online on www.kaccounting.com or on any of the four\
             iOS and Android apps, Kaccounting makes it easy to run your business.")
        st.write("Our accounting software offers the possibility to connect different companies\
             and users into one account. You can use this to exchange your data instantly with \
             your partner, colleague or accountant.")
        info = st.button("More...")
        if info:
            st.balloons()
    elif page == "Images":
        st.title("Images")
        pics = {
            "Cat": "https://cdn.pixabay.com/photo/2016/09/24/22/20/cat-1692702_960_720.jpg",
            "Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
            "Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg"
        }
        pic = st.selectbox("Picture choices", list(pics.keys()), 0)
        st.image(pics[pic], use_column_width=True, caption=pics[pic])
    elif page == "Invoices":
        st.title("Invoices")
        st.header("Invoincing module")
        bulstat = st.text_input('Enter Bulstat')
        readButton = st.button("Get data")
        if readButton:
            getDataFromDb(bulstat)

@st.cache
def load_data():
    df = data.cars()
    return df

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    st.write(graph)

def getDataFromDb(bulstat):
    conn = db.createConnection('databases\\companies.db')
    data = db.readMainData(conn, bulstat)
    if len(data) > 0:
        df = pd.DataFrame(data)
        df.columns = ["ID", "Bulstat", "Name", "Created on"]
        st.write(df)
    else:
        createNewCompany(bulstat)

def createNewCompany(bulstat):
    st.write("No company with this bulstat exists. Create now?")
    companyName = st.text_input('Enter company name')
    createButton = st.button("Create")
    if createButton:
        newCompany = contragents.Contragent(bulstat=bulstat, name=companyName)
        st.write("New record created for {}!".format(companyName))

if __name__ == "__main__":
    main()
