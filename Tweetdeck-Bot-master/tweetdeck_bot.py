"""
    tweetdeck_bot.py, a project by rhaeyx
    Please consider giving this repo a star. 
    https://github.com/rhaeyx/Tweetdeck-Bot

    Contents:
        tweetdeck_bot.py - source code
        bot.py(this) - file to execute
        tweets.txt - Example text file
"""

from bot_scripts.tweetdeck import tweetdeck

# Set username and password
bot = tweetdeck(username='Eliot??????', password='George??????')

# Start bot. Default values are just placeholders, change as you want.
"""
bot.start(starting_date='12-09-2019', FORMAT: MM-DD-YYYY
          time_slots = [(8, 30, 'PM'), FORMAT: (hour, min, period) period is 'AM' or 'PM'
                        (5, 30, 'PM'),
                        (6, 30, 'PM'), 
                        (7, 30, 'PM')],
          source='tweets.txt') 
          # Source file: file_name.txt, make sure to place the file in same folder, together with this
          # file and tweetdeck_bot.py
"""

# EXAMPLE:
bot.start(starting_date='08-25-2022',
          time_slots = [(1, 00, 'AM')],
          source='scheduledtweets.txt')

