from bs4 import BeautifulSoup
import requests

# html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35").text
# soup = BeautifulSoup(html_text, 'lxml')
# thing = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# thing_name = thing.find('h3', class_='joblist-comp-name').text.replace('(More Jobs)', '')
#
# print(thing_name)

html_text = requests.get("https://podcasts.apple.com/us/podcast/last-podcast-on-the-left/id437299706").text
soup = BeautifulSoup(html_text, 'lxml')
ep_element = soup.find_all('li', class_='tracks__track tracks__track--podcast')
# title = ep_element.find('h2', class_='tracks__track__headline spread').text
records = []
for ep in ep_element:
    title = ep.find('h2', class_='tracks__track__headline spread').text.replace('\n', '')
    records.append(title)


for number, record in enumerate(records, start=1):
    print(number, record)