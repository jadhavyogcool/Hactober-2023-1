# import html 
import html 

s = '<html><head></head><body><h1>This is python</h1></body></html>'
temp = html.escape(s) 
# Using html.unescape() method 
gfg = html.unescape(temp) 

print(gfg) 
