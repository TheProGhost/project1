import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# addr = "1FvzCLoTPGANNjWoUo6jUGuAG3wg1w4YjR"
def Scams_Reports(addr):
    url = "https://www.bitcoinwhoswho.com/search?keyword=" + addr
    webpage = requests.get(url)

    for i in range(3):
        if webpage.text.find("Loading") > -1:
            webpage = requests.get(url)
            time.sleep(0.8)
        else:
            break

    soup = BeautifulSoup(webpage.text, "html.parser")

    scams = {}
    scams_report = ""
    website_report = ""
    website_appear = {}
    scams_table = ""
    website_table = ""

    # getting scam reports 
    scamReport = soup.find('span', {'class': 'top_scam_alert'})
    # print(scamReport.text)

    # getting general info 
    gen_info = soup.find('div', {'id': 'top_report_box'})
    info = []
    for i in gen_info.text.split('\n'):
        if i != '':
            info.append(i)



    # getting scam reports

    if scamReport.text == 'Scam Alert: None':
        scams_report = None
    else:

        scams_name = []
        url_ = []
        dates = []

        div = soup.find('div', {'id': 'scam_records_table'})
        scam_name = div.findAll('div', {'class': 'col-md-4 srtr_div'})
        scams_report = str(len(scams_name) - 1)

        for i in scam_name:
            scams_name.append(i.text)

        scams_name = scams_name[1:]

        urls = div.findAll('div', {'class': 'col-md-5 srtr_div'})
        for i in urls:
            url_.append(i.text)
        
        url_ = url_[1:]

        date_ = div.findAll('div', {'class': 'col-md-1 srtr_div'})
        for i in date_:
            # if i.text != '' and i.text != '\n' and i.text != '\n\n' and i.text != '\n\n\n':
            dates.append(i.text)

        dates = dates[1:]


        scams["Name"] = scams_name
        scams["Urls"] = url_
        scams["Date"] = dates

        df = pd.DataFrame(data=scams)
        df = df.fillna(' ')
        scams_table = df.to_html(border = 0, classes="table table-stripped", index=False,render_links=True, justify="left")



    # getting website appearences


    if info[3] == '0':
        website_report = None
    else:

        dates_ = []
        description = []
        more = []
        website_url = []
        country = []


        websites = soup.find('div', {'id': "url_bitcoin_found_table"})
        dates = websites.findAll('div', {'class': 'col-md-1'})
        website_report = str(len(dates) - 1)

        for i in dates:
            dates_.append(i.text)
        
        dates_ = dates_[1:]

        description_more = websites.findAll('div', {'class': 'col-md-2'})
        count = 0
        for i in description_more:
            if count % 3 == 0:
                # print(f'Description: {i.text}')
                description.append(i.text)
                count += 1
            elif count % 3 == 1:
                # print(f'More : {i.text}')
                more.append(i.text)
                count += 1
            else:
                # print(f'country {i.text}')
                country.append(i.text)
                count += 1

        description = description[1:]
        more = more[1:]
        country = country[1:]

        urls = websites.findAll('div', {'class': 'col-md-5'})
        for i in urls:
            website_url.append(i.text)

        website_url = website_url[1:]

        website_appear["Dates"] = dates_
        website_appear["Description"] = description
        website_appear["More"] = more
        website_appear["Urls"] = website_url
        website_appear["Country"] = country

        df = pd.DataFrame(data=website_appear)
        df = df.fillna(' ')
        website_table = df.to_html(border = 0, classes="table table-stripped", index=False,render_links=True, justify="left")


    return scams_report, scams_table, website_report, website_table