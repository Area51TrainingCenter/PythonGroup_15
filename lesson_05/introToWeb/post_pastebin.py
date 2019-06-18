import requests

url = 'http://pastebin.com/api/api_post.php'
api_key = '1857fade8a3b92b18bf741942700c2f7'
source_code = 'print("Hello World!")'
data = {
    'api_dev_key': api_key,
    'api_option': 'paste',
    'api_paste_code': source_code,
    'api_paste_format': 'python'
}
r = requests.post(url=url, data=data)
print(r.text)

