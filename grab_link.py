# -*- coding: utf-8 -*-

#import urllib;
import urllib2;
import re; 
import os;
import time;

#src_url='http://fenxiang.qq.com/share/index.php/share/share_c/index/3SyKv1dyd~FIc1OKSq7Sz~8UIdPlo3AyiiY';
#title='';
def get_content(src_url):
  #re_string='qhref="(?P<url>.*?)"';
  #re_string='<h2>.*?\sqhref="(?P<url>.*?)"\sfilehash=.*?\stitle="(?P<title>.*?)"</h2>';
  re_string='<h2>(?P<h2>.*?)</h2>';
  re_url='qhref="(?P<url>.*?)"';
  re_url_title='title="(?P<title>.*?)"';
  re_title='<h1>(?P<title>.*?)</h1>';
  req=urllib2.urlopen(src_url);
  resp=req.read();
  found=re.finditer(re_string,resp,re.S);
  title_found=re.search(re_title,resp);
  savepath=title_found.group('title')+".txt";
  if os.path.isfile(savepath):
    savepath=title_found.group('title')+time.strftime('%Y%m%d%H%I%M%S',time.localtime(time.time()))+".txt"
  with open(savepath,'a+') as save_file:
    for item in found:
      #print item.group('h2');
      h2_content=item.group('h2');
      title_found=re.search(re_url_title,h2_content,re.S);
      url_found=re.search(re_url,h2_content,re.S);
      save_file.write(title_found.group('title'));
      save_file.write('\n');
      save_file.write(url_found.group('url'));
      save_file.write('\n');
  print 'ok';
      
if __name__=='__main__':
  print "请输入链接："
  src_url=str(raw_input(u"url:"));
  get_content(src_url);

  