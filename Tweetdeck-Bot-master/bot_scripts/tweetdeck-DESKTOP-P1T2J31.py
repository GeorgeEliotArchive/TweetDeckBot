from time import sleep
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class tweetdeck:

    def __init__(self, username='user', password='password'):
        self.username = username
        self.password = password

    # Set up
    def open_tweetdeck(self):
        self.chrome = webdriver.Chrome('chromedriver.exe')
        self.chrome.get('https://tweetdeck.twitter.com')

    def login(self):

        wait = WebDriverWait(self.chrome, 10)

        # Click login
        # WebDriverWait(self.chrome, 1).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.Button.Button--primary'))).click()
        # self.chrome.find_element_by_link_text('Log in').click()
        # self.chrome.find_element(By.LINK_TEXT, 'Log in').click()
        # sleep(1)

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log in'))).click()

        # Type in username
        #username = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        #username = self.chrome.find_element_by_xpath('//*[@id="react-root"]/div/div/div/div/div/div/div/div[2]/div/div[5]/label/div/div[2]/div/input')
        # username = self.chrome.find_element_by_xpath('//*[@id="react-root"]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        # username.send_keys(self.username)
        # self.chrome.find_element_by_css_selector('.r-fdjqy7').send_keys(self.username)
        # self.chrome.find_element(By.CSS_SELECTOR, '.r-fdjqy7').send_keys(self.username)
        # sleep(1)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r-fdjqy7'))).send_keys(self.username)

        # Click Next
        # self.chrome.find_elements_by_css_selector('.r-a023e6')[4].click()
        # self.chrome.find_elements(By.CSS_SELECTOR, '.r-a023e6')[4].click()
        # sleep(1)

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.r-a023e6')))[4].click()

        # Type in password
        # password = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
        # password.send_keys(self.password)
        # self.chrome.find_elements_by_css_selector('.r-fdjqy7')[1].send_keys(self.password)
        # self.chrome.find_elements(By.CSS_SELECTOR, '.r-fdjqy7')[1].send_keys(self.password)
        # sleep(1)

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.r-fdjqy7')))[1].send_keys(self.password)

        # Log in
        # sign_in = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
        # sign_in.click()

        # self.chrome.find_elements_by_css_selector('.r-a023e6')[3].click()
        # self.chrome.find_elements(By.CSS_SELECTOR, '.r-a023e6')[3].click()
        # sleep(1)

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.r-a023e6')))[3].click()

    def set_month(self, current_month, target_month, current_year, target_year):
        # Calculate the difference between the current month in the calendar and the
        # target month, then click the button to change the months.

        months_dict = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4,
                       'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8,
                       'September': 9, 'October': 10, 'November': 11, 'December': 12}

        current_month = months_dict[current_month]
        current_year = int(current_year)

        clicks = target_month - current_month
        month_btn = ''

        if clicks == 0:
            return
        elif clicks > 0:
            # month_btn = self.chrome.find_element_by_xpath('//*[@id="next-month"]')
            month_btn = self.chrome.find_element(By.XPATH, '//*[@id="next-month"]')
        else:
            # month_btn = self.chrome.find_element_by_xpath('//*[@id="prev-month"]')
            month_btn = self.chrome.find_element(By.XPATH, '//*[@id="prev-month"]')
            if target_year != current_year:
                diff = target_year - current_year
                clicks += (12 * diff)

            clicks = abs(clicks)

        for _ in range(clicks):
            month_btn.click()

    def fill_up(self, text, hour, minute, period, month, day, year):
        """
            fill_up(text, hour, minute, period, month, day, year)

            arg types:
            hour - int        day - int
            minute - int      year - int
            period - str      month - int
        """

        # tweet_btn = self.chrome.find_element_by_css_selector('.tweet-button')
        tweet_btn = self.chrome.find_element(By.CSS_SELECTOR, '.tweet-button')
        tweet_btn.click()

        # textbox = self.chrome.find_element_by_css_selector(
        #     'div.antiscroll-inner.scroll-v.scroll-styled-v.padding-h--15 > div.position-rel.compose-text-container.padding-a--10.br--4 > textarea')
        # textbox = self.chrome.find_element_by_css_selector('.compose-text')
        textbox = self.chrome.find_element(By.CSS_SELECTOR, '.compose-text')
        textbox.send_keys(text)

        # sched_tweet = self.chrome.find_element_by_css_selector(
        #     'div.antiscroll-inner.scroll-v.scroll-styled-v.padding-h--15 > div.js-scheduler > button')

        # sched_tweet = self.chrome.find_elements_by_css_selector('.btn-on-blue')[1]
        sched_tweet = self.chrome.find_elements(By.CSS_SELECTOR, '.btn-on-blue')[1]
        self.chrome.execute_script('arguments[0].click()', sched_tweet)

        # element = self.chrome.find_element_by_css_selector('.compose .antiscroll-scrollbar')
        # self.chrome.execute_script("arguments[0].setAttribute('style', 'top:22.3333px')", element)

        # hour_box = self.chrome.find_elements_by_css_selector('.cal input')[0]
        hour_box = self.chrome.find_elements(By.CSS_SELECTOR, '.cal input')[0]
        hour_box.send_keys('\b\b'+str(hour))

        # minute_box = self.chrome.find_elements_by_css_selector('.cal input')[1]
        minute_box = self.chrome.find_elements(By.CSS_SELECTOR, '.cal input')[1]
        minute_box.send_keys('\b\b'+str(minute))

        # period_btn = self.chrome.find_element_by_css_selector('.Button--small')
        period_btn = self.chrome.find_element(By.CSS_SELECTOR, '.Button--small')
        if period_btn.text != period.upper():
            period_btn.click()
            sleep(0.5)

        # month_text = self.chrome.find_element_by_xpath('//*[@id="caltitle"]').text
        # month_text = self.chrome.find_element_by_id('caltitle').text
        month_text = self.chrome.find_element(By.ID, 'caltitle').text
        current_month, current_year = month_text.split(' ')
        self.set_month(current_month, month, current_year, year)

        # date = self.chrome.find_element_by_link_text(str(day))
        date = self.chrome.find_element(By.LINK_TEXT, str(day))
        date.click()
        date = self.chrome.find_element(By.LINK_TEXT, str(day))
        date.click()

        # submit_btn = self.chrome.find_element_by_css_selector('.padding-h--12')
        submit_btn = self.chrome.find_element(By.CSS_SELECTOR, '.padding-h--12')
        submit_btn.click()
        sleep(0.5)

    def start(self, source, starting_date, time_slots):

        """
            start(source='source_file_name.txt',
                  starting_date='MM-DD-YYYY',
                  time_slots=[(hour, min, 'AM'/'PM'), (hour, min, 'AM'/'PM'),
                              (hour, min, 'AM'/'PM'), (hour, min, 'AM'/'PM')])

            arg types:
            source - string
            starting_date - string
            time_slots - list of tuples, each tuple with 3 elements
        """

        maximum_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        print("""
            |=============================================|
            | Welcome to TweetDeck-Bot.py by rhaeyx       |
            | Please consider giving this repo a star.    |
            | https://github.com/rhaeyx/Tweetdeck-Bot     |
            |=============================================|
        """)

        print('[TweetDeck_Bot] Starting bot...')

        self.open_tweetdeck()
        sleep(5)

        print('[TweetDeck_Bot] Logging in...')
        self.login()
        sleep(5)
        print('[TweetDeck_Bot] Logged in.')

        starting_date = starting_date.split('-')
        month = int(starting_date[0])
        day = int(starting_date[1])
        year = int(starting_date[2])

        counter = 1

        print('[TweetDeck_Bot] Reading tweets to be scheduled...')
        lines = ''
        with open(source, 'r') as f:
            f = f.read()
            lines = f.split('\n')

        print('[TweetDeck_Bot]', len(lines), 'tweets found.')
        print('[TweetDeck_Bot] Removing text, that exceed the twitter character limit...')
        char_limit = 280
        for line in lines:
            if len(line) > char_limit:
                lines.remove(line)
        print('[TweetDeck_Bot]', len(lines), 'total number of tweets after purge.')

        print('[TweetDeck_Bot] Scheduling...')


        while len(lines) != 0:
            print('[TweetDeck_Bot] Tweets for:', '-'.join([str(month), str(day), str(year)]))
            for time_slot in time_slots:

                if len(lines) == 0:
                    break

                hour = time_slot[0]
                minute = time_slot[1]
                period = time_slot[2]

                #random_index = randint(0, len(lines)-1)
                line = lines.pop(0)
                print('[TweetDeck_Bot] Tweet #'+str(counter), 'will be tweeted on ',':'.join([str(hour), str(minute)]), period)

                self.fill_up(line, hour, minute, period, month, day, year)
                counter += 1
                sleep(1)
                

            if day == maximum_days[month]:

                if month == 12:
                    month = 1
                    day = 1
                    year += 1
                else:
                    month += 1
                    day = 1
            else:
                day += 1

        print('[TweetDeck_Bot] Total number of tweets:', counter)
