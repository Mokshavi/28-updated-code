from simple.WebScrapy import Scrapy
from simple.config import Config
con=Config()
scrapy=Scrapy()
#scrapy.login(con.session(),con.Headers(),con.credentials())
scrapy.boards(con.session())
#s1=scrapy.scrapy_parser(con.session(),scrapy.boards(con.session()))
#print(s1))