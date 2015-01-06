import requests
import BeautifulSoup
import re

def get_math(subj):
    """requests math page and returns link to document.

    uses requests library to call the math page. searches for google
    doc link to assignment. parses link to create a useable link to
    assignment. returns useful url

    """

    page = requests.get(subj)
    soup = page.text.encode("latin-1", "ignore")
    soup = BeautifulSoup.BeautifulSoup(soup)
    for a in soup.findAll('a', href=True):
        if "docs.google.com" in a['href']:
            math_doc = a['href']
    start = math_doc.find("srcid=")
    return "https://drive.google.com/viewerng/viewer?a=v&pid=sites&"+math_doc[start:]

def get_science(subj):
    """requests science page and returns latest info.

    

    """

    page = requests.get(subj)
    soup = page.text.encode("latin-1", "ignore")
    soup = BeautifulSoup.BeautifulSoup(soup)
    for a in soup.findAll("a", href=True):
        if "science-assignments" in a['href'] and "xml" not in a['href']:
            science_page = a['href']
            break
    assignment_page = requests.get("https://sites.google.com/"+science_page)
    soup2 = assignment_page.text.encode("latin-1", "ignore")
    soup2 = BeautifulSoup.BeautifulSoup(soup2)
    return soup2.findAll("table")[-1].getText("\n")

def get_english(subj):
    """requests english page and returns latest info"""

    page = requests.get(subj)
    soup = page.text.encode("latin-1", "ignore")
    soup = BeautifulSoup.BeautifulSoup(soup)
    return soup.findAll("div","paragraph")[0].getText("\n")

def get_world(subj):
    """ need to look at google calendar API"""
    pass

def main():

    math = "https://sites.google.com/a/kealing.org/ms-girardeau-sixth-grade-math/homework-assignments"
    world = "https://sites.google.com/a/austinisd.org/mr-shoaf-s-classroom/world-cultures"
    science = "https://sites.google.com/a/austinisd.org/mcdonald-6th-grade-science/home/science-assignments"
    english = "http://stewartkealing.weebly.com/magnet-6th-grade-english.html"
    math_link = get_math(math)
    science_info = get_science(science)
    english_info = get_english(english)

#    get_world(world)


if __name__=="__main__":
    main()
