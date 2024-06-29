from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st

st.title('Web scraper')
st.write('fetch and display data from flipkart.')



if st.button('Scrape'):
    product_name = []
    prices = []
    description = []


    for i in range(2,10):
        url = 'https://www.flipkart.com/search?q=mobiles+under+40000&otracker=search&otracker1s=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)


        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_ = "KzDlHZ")
        for i in names:
            name = i.text
            product_name.append(name)

        price = soup.find_all("div", class_ = "Nx9bqj _4b5DiR")
        for i in price:
            name = i.text
            prices.append(name)

        desc = soup.find_all("ul", class_ = "G4BRas" )
        for i in desc:
            name = i.text
            description.append(name)

    min_length = min(len(product_name), len(prices), len(description))
    product_name = product_name[:min_length]
    prices = prices[:min_length]
    description = description[:min_length]

    df = pd.DataFrame({
        "product name": product_name,
        "price": prices,
        "description": description
    })

    st.write('Data Scraped Successfully')
    st.write(df)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='scraped_data.csv',
        mime='text/csv',
    )



    # df.to_csv("flipkart mobile under 40000.csv")
