from requests import session
from bs4 import BeautifulSoup

cookies = {
    '__utma': '51854390.1771337125.1462167971.1463759106.1463759106.1',
    '__utmb': '51854390.4.10.1463759106',
    '__utmc': '51854390',
    '__utmt': '1',
    '__utmv': '51854390.100-1|2=registration_date=20141201=1^3=entry_date=20141201=1',
    '__utmz': '51854390.1463759106.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    'cap_id': 'NjJiMGU3YjE4MGI1NDMyZjg0N2EwZjVmN2Y1YWIxYTk=|1463759105|d2477e25d27383609ec6bfa74a11e64ae3c0f15e',
    'l_cap_id': 'OWE0OWM3Nzc1MTVmNDNkNzliNTVlNDFlZTk1YjUzMWM=|1463759105|507298aa58e047922f0d125718ae4ab175b329a3',
    'l_n_c': '1',
    'login': 'ZWM4YTYxZTRlZWI1NDhkZmEyNzdmNjZhZTYxOWYxNmE=|1463759112|0da618063a64a1d44485f47981e0188b04ebe970',
    'z_c0': 'Mi4wQUFEQVlKVkNBQUFBTUFEdkxQekRDUmNBQUFCaEFsVk5DTDVtVndCUUdTN1p1QkpXLWpwS29QVEZPd1VhZm9wWkNR|1463759112|9256736622a3bcf2ab4ec1b246605fc3208b92a5'
}

s = session()
url = 'https://www.zhihu.com/question/26522101#answer-36117721'

content = s.get(url, cookies=cookies).text

print(type(content))

b = BeautifulSoup(content, 'html5lib')
print(b.find('div', class_='zg-wrap zu-main clearfix with-indention-votebar')['data-urltoken'])
print(b.find('h2', class_='zm-item-title zm-editable-content').contents[0])

with open('question.html', 'w', encoding='utf-8') as f:
    f.write(content)


