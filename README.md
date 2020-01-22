# Crawler-StackOverflow
- Extracted from stackoverflow.com the 10 newest Android-related questions and the 10 most voted Android-related questions that are created in the past week.
- Writtern in Python 3.7

### Features
1. Extracted the 10 newest Android-related questions without duplicated ones.

2. Extracted the 10 most voted Android-related questions posted in the last 7 days without duplicated ones.

3. Displayed the titles of the extracted questions on a website.

4. Updated the web content when clicking the update button and showed the update time.(NEW)
  
4. Displayed the full text of question in a drop-down box when clicking on the question title.

5. Displayed key attributes of every question under its title, such as answer number, vote number and creat time.(NEW)
  
6. Saved the 10 newest and 10 most voted questions in csv files respectively.(NEW)

### Prerequisites
- pip install requests

- pip install beautifulsoup4

- pip install dorminate

- pip install flask

### How to Run
1. Run 'python server.py' in cmd.
2. Open 'http://127.0.0.1:5000/' in web browser. (Tested by Firefox and Chrome)
3. Waite for a few seconds until 'Finished!' is printed in terminal.
4. One can update the data by clicking on the button 'Update'.
