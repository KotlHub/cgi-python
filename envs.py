#! "C:/Python311/python.exe"

import os
# os.environ -- dict із змінними оточенням (ім'я - значення)
keys = ['REQUEST_METHOD', 'QUERY_STRING', 'REQUEST_URI', 'REMOTE_ADDR']
 
envs = "<ul>" + "".join("<li>%s = %s</li>" %(k,v) for k,v in os.environ.items() if k in keys) + "</ul>"

querry_params = {k: v for k,v in (pair.split('=') for pair in os.environ["QUERY_STRING"].split('&'))}

lang = querry_params['lang']
resource = {
    'uk' : 'Вітання',
    'en' : 'Greeting',
    'de' : 'Herzlich willkommen'
}

if not lang in resource:
    lang = 'uk'

print( "Content-Type: text/html")
print( "") # заголовки від тіла відокремлюються порожнім рядком
print( f"""<!doctype html>
      <html>
        <head>
            <title>
                Python-Linchevsky
            </title>
        </head>
        <body>
            <h1>
                {resource[lang]}
            </h1>
            <pre>
            {querry_params}
            </pre>
        </body>
      </html>
      """)