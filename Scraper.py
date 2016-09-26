from mechanize import Browser
from bs4 import BeautifulSoup
br = Browser()
br.open('https://my.sa.ucsb.edu/gold/login.aspx')
br.select_form(nr=0)

# br.form['ctl00$pageContent$userNameText'] = raw_input("Enter your Username")
# br.form['ctl00$pageContent$passwordText'] = raw_input("Enter your Password")


br.submit()

br.open('https://my.sa.ucsb.edu/gold/StudentSchedule.aspx')

soup = BeautifulSoup(br.response().read(), "html.parser")


# num=0
# nameTag = soup.find("span", {"id": "pageContent_CourseList_CourseHeadingLabel_" + str(num)})
# while nameTag!=None:
#     #timeTag= soup.find("table", {"id": "pageContent_CourseList_MeetingTimesList_" + str(num)})
#
#     print nameTag.getText()
#     #print timeTag
#
#     num+=1
#     nameTag = soup.find_next("span", {"id": "pageContent_CourseList_CourseHeadingLabel_" + str(num)})

tags = soup.find_all("span", {"id": "pageContent_CourseList_CourseHeadingLabel_0"})
print tags
