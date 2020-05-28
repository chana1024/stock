import sys

from scrapy.cmdline import  execute
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))) #大括号内即把该文件路径变为绝对路径
execute(["scrapy", "crawl", "finance"])  #以项目example为例