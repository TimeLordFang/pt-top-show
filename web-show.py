from flask import Flask,render_template,url_for
import sqlite3
import time

app = Flask(__name__)

@app.route('/')
def web_show():
    conn = sqlite3.connect('pttop.db')
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute("select * from PTTOP")
    x = cur.fetchall()
    #print(x)
    democss = url_for('static', filename='style.css')
    return render_template('hello.html',x_list = x,demoCSS=democss)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
