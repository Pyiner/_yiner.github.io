#coding=utf-8
import requests
import json
r = requests.get('http://www.pyiner.com/all/')
print r.content
al = json.loads(r.content)
a = '---\nlayout: default\ntitle: %s\n---\n'
for i in al:
    with open('2014-01-01-%s.md'%i['url'],'w') as f:
        f.write(a%i['title'].encode('utf-8'))
        f.write(i['content'].encode('utf-8'))
