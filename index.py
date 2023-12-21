#!C:/Users/Admin/AppData/Local/Programs/Python/Python312/python.exe

import os
# os.environ -- dict із змінними оточенням (ім'я - значення)
keys = ['REQUEST_METHOD', 'QUERY_STRING', 'REQUEST_URI', 'REMOTE_ADDR']
 
envs = "<ul>" + "".join("<li>%s = %s</li>" %(k,v) for k,v in os.environ.items() if k in keys) + "</ul>"
print( "Content-Type: text/html")
print( "") # заголовки від тіла відокремлюються порожнім рядком
print( """<!doctype html>
      <html>
        <head>
            <title>
                python 201
            </title>
        </head>
        <body>
            <h1>
                CGI працює
            </h1>
            <button id="auth-button" onclick="authClick()">Auth</button>
            <script>
                function authClick() {
                    fetch("/auth?login=alpha&password=beta")
                    .then(r => r.text())
                    .then(console.log)
                }
            </script>
        </body>
      </html>
      """)