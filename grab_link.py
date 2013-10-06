# -*- coding: utf-8 -*-

#import urllib;
import urllib2;
import re; 
import os;

src_url='http://fenxiang.qq.com/share/index.php/share/share_c/index/3SyKv1dyd~FIc1OKSq7Sz~8UIdPlo3AyiiY';
re_string='qhref="(?P<url>.*?)"';
re_title='<h1>(?P<title>.*?)</h1>';
req=urllib2.urlopen(src_url);
resp=req.read();
found=re.finditer(re_string,resp);
title_found=re.search(re_title,resp);
savepath=title_found.group('title')+".txt";
#print savepath;
#print found.group('url');
with open(savepath,'a+') as save_file:
  for url in found:
    save_file.write(url.group());
    save_file.write('\n');
    
