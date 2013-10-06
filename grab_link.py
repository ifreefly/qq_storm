# -*- coding: utf-8 -*-

#import urllib;
import urllib2;
import re; 
import os;
import time;

#src_url='http://fenxiang.qq.com/share/index.php/share/share_c/index/3SyKv1dyd~FIc1OKSq7Sz~8UIdPlo3AyiiY';
def get_content(src_url):
  re_string='qhref="(?P<url>.*?)"';
  re_title='<h1>(?P<title>.*?)</h1>';
  req=urllib2.urlopen(src_url);
  resp=req.read();
  found=re.finditer(re_string,resp);
  title_found=re.search(re_title,resp);
  savepath=title_found.group('title')+".txt";
  #print savepath;
  #print found.group('url');
  if os.path.isfile(savepath):
    savepath=title_found.group('title')+time.strftime('%Y%m%d%H%I%M%S',time.localtime(time.time()))+".txt"
  with open(savepath,'a+') as save_file:
    for url in found:
      save_file.write(url.group('url'));
      save_file.write('\n');
    
print "请输入链接："
src_url=str(raw_input(u"url:"));
get_content(src_url);
