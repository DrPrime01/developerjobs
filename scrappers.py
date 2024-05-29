from bs4 import BeautifulSoup
import requests

site = requests.get("https://remote.co/")
soup = BeautifulSoup(site.text, "lxml")

def remoteco(href):
    """Get all links"""
    r = requests.get(href)
    s = BeautifulSoup(r.text, "lxml")
    jobs = []
    for link in s.find_all("a", class_="card"):
        job_title = link.p.span.find(string=True, recursive=False).strip()
        if "frontend" in job_title.lower():
            company_tag = link.find("p", class_="m-0 text-secondary")
            company_name = company_tag(string=True, recursive=False)[0].split("|")[0].strip()
            jobs.append({
                "job_title": job_title,
                "company": company_name,
                "href": f"https://remote.co/remote-jobs/developer{link.get('href')}",
                "posted": link.date.text
            })
    print(jobs)

def weworkremotely(href):
    """Scraps developer jobs from weworkremotely.com"""
    r = requests.get(href)
    bs = BeautifulSoup(r.text, "lxml")
    jobs_section = bs.find("section", id="category-2")
    jobs = []
    for job in jobs_section.find_all("li", class_="feature"):
        jobs.append({
            "job_title": job.find("span", class_="title").text.strip(),
            "company": job.find("span", class_="company").text.strip(),
            "href": f"https://weworkremotely.com{job.find('a')['href']}",
            "posted": ""
        })
    print(jobs)

remoteco("https://remote.co/remote-jobs/developer/")
weworkremotely("https://weworkremotely.com/")