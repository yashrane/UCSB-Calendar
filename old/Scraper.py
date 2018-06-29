from mechanize import Browser
from bs4 import BeautifulSoup

from parse import parse

def splitArray(scheduleArray):
    newArray = []
    for classinfo in scheduleArray:
        if len(classinfo) > 4:
            newArray.append(classinfo[:4])
            newArray.append([classinfo[0]]+classinfo[4:])
        else:
            newArray.append(classinfo)
    return newArray


br = Browser()
br.open('https://my.sa.ucsb.edu/gold/login.aspx')
br.select_form(nr=0)

br.form['ctl00$pageContent$userNameText'] = raw_input("Enter your Username :")
br.form['ctl00$pageContent$passwordText'] = raw_input("Enter your Password :")




br.submit()

br.open('https://my.sa.ucsb.edu/gold/StudentSchedule.aspx')

soup = BeautifulSoup(br.response().read(), "html.parser")

scheduleInfo=[]
currentClass=-1
previous = ""

tags = soup.find_all(["span","td"])
for tag in tags:
    if "id" in tag.attrs and "pageContent_CourseList_CourseHeadingLabel" in tag["id"]:
        scheduleInfo.append([tag.getText(strip=True)])
        currentClass+=1
    if "class" in tag.attrs  and ("clcellprimary" in tag["class"] or "clcellprimaryalt" in tag["class"]) and ("AM-" in  tag.getText() or "PM-" in tag.getText()):
        scheduleInfo[currentClass].append( tag.getText(strip=True))
        scheduleInfo[currentClass].append(previous)
    if "style" in tag.attrs and "color: #336699 !important; text-align: left;" in tag["style"] and"Location:" in tag.getText():
        scheduleInfo[currentClass].append(tag.getText(strip=True))
    previous=tag.getText(strip=True)

scheduleInfo=splitArray(scheduleInfo)



parser = parse ()
parser.place_array_in_calendar(scheduleInfo)
