from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import requests

# retrieve data from pods.csv and converts to usable dictionary
def retrieve_dict():
    get_dict_file = open('pods.csv', 'r')
    dict_reader = csv.reader(get_dict_file)

    for row in dict_reader:
        csv_dict[row[0]] = row[1]

    return

# adds new podcast via user input
def add_new():
    new_pod_name = input("Enter the name of the podcast: ")
    new_pod_link = input("Enter the apple podcast link: ")
    new_csv_line = (new_pod_name + ',' + new_pod_link)

    return new_csv_line

# TODO: implement wait for redirect so url don't become borked, OR implement function to update url after redirect
# https://stackoverflow.com/questions/40002826/wait-for-page-redirect-selenium-webdriver-python

csv_dict = {}

while True:
    retrieve_dict()
    # TODO trying to fix --- [FIXED]
    print(list(csv_dict.keys()))
    # print(csv_dict.keys())


    play_now = input("Enter which podcast to play: (addnew: to add new podcast)\n")

    # allows user to add new podcast
    if play_now == "addnew":

        # appends csv with new podcast
        with open("pods.csv", 'a') as update_csv:
            update_csv.write("\n" + add_new())
            continue

    # passes along the selected podcast
    if play_now in csv_dict:
        pod_link = csv_dict.get(play_now)
        break

# collects html episode elements from selected podcast link
html_text = requests.get(pod_link).text
soup = BeautifulSoup(html_text, 'lxml')
ep_element = soup.find_all('li', class_='tracks__track tracks__track--podcast')

# creates numbered list of most recent episode titles
title_list = []
for ep in ep_element:
    title = ep.find('h2', class_='tracks__track__headline spread').text.replace('\n', '')
    title_list.append(title)

for number, record in enumerate(title_list, start=1):
    print(number, record)


# asks user which episode they would like to play?
print('\n')
episode = str(input("Which episode? \n"))

str_xpath1 = ('/html/body/div[5]/main/div[2]/div/section[1]/div/div[2]/div[4]/div/ol/li[')
str_xpath2 = (']/div/div/ul[2]/li[1]')
# xpath to episode desired by user
str_xpath = str(str_xpath1 + episode + str_xpath2)

driver = webdriver.Chrome(executable_path='C:/Users/RyanL/PycharmProjects/pythonProject/Projects/Poddity/chromedriver.exe') # make sure this is upto date w chrome browser
driver.get(pod_link)  # url

time.sleep(1) # needs a time delay or else, the element is clicked before it loads functionalilty
element = driver.find_element(By.XPATH, str_xpath)
element.click()
