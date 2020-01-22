import requests
from bs4 import BeautifulSoup
import urllib
from dominate.util import raw
from dominate.tags import *

def fun_ResultSet2List(rs):
    r=[]
    for i in rs:
        r.append(i.get_text())
    return r
def fun_Tags2Str(l):
    string=""
    for word in l:
        string = string + word + "; "
    return string
def fun_FetchFromSOF(gURL):
    data = []
    site = requests.get(gURL)
    if site.status_code == 200:
        content = BeautifulSoup(site.content, 'html.parser')
        questions = content.select('.question-summary')[0:10:1]
    
        for question in questions:
            topic = question.select( '.question-hyperlink')[0].get_text()
            answers = question.select('.status')[0].get_text()
            votes = question.select('.votes')[0].get_text()
            askedtime = question.find(class_='started fr').select('.relativetime')[0].get_text()
            url = urllib.parse.urljoin('https://stackoverflow.com', question.select( '.question-hyperlink')[0].get('href'))
            q_site = requests.get(url)
            if q_site.status_code == 200:
                q_content = BeautifulSoup(q_site.content,'html.parser')
                q_text = str(q_content.select('.post-text')[0])
                q_tags = fun_ResultSet2List(q_content.find(class_='post-taglist').select('.post-tag'))
            new_data = {"topic": topic, "url": url, "answers":answers, "votes":votes,"question":q_text,"tags":q_tags,"askedtime":askedtime}
            data.append(new_data)
        print('Successfully Fetching Data From ',gURL)
    else:
        print('Cannot Fetching Data From ',gURL)
    return data

data_MostVoted=fun_FetchFromSOF('https://stackoverflow.com/search?tab=votes&q=is%3aq+[android]+duplicate%3ano+created%3a7d..')
data_Newest=fun_FetchFromSOF('https://stackoverflow.com/search?tab=newest&q=[android]+duplicate%3ano')

h = html()
h_head = h.add(head(link(rel='stylesheet', href='./mycss.css')))
h_body = h.add(body())
h_body_div = h_body.add(div(id='content'))
with h_body_div:
    h1(u'The 10 newest Android-related questions in Stack Overflow.')
    for idx,data in enumerate(data_Newest):
        details(
            summary(
                str(idx+1)+'. '+data['topic'][4:],
                a('Links',href=data['url']),
                p(
                    a('Answers: ',list(filter(str.isdigit,data['answers']))," "),
                    a('Votes: ',list(filter(str.isdigit,data['votes']))," "),
                    a('Tags: ',fun_Tags2Str(data['tags'])),
                    a('Asked Time: ',data['askedtime'])
                )
            ),
            blockquote(raw(data['question'])),
            raw('<br/><hr/><br/><br/>')
           
        )

    h1(u'The 10 most voted Android-related questions posted in the past week in Stack Overflow.')
    for idx,data in enumerate(data_MostVoted):
        details(
            summary(
                str(idx+1)+'. '+data['topic'][4:],
                a('Links',href=data['url']),
                p(
                    a('Answers: ',list(filter(str.isdigit,data['answers']))," "),
                    a('Votes: ',list(filter(str.isdigit,data['votes']))," "),
                    a('Tags: ',fun_Tags2Str(data['tags'])),
                    a('Asked Time: ',data['askedtime'])
                )
            ),
            blockquote(raw(data['question'])),
            raw('<br/><hr/><br/><br/>')
        )

with open('test.html','w',encoding='utf-8') as f:
    f.write(h.render())
