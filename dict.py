from flask import Flask, render_template, request
import requests
import sqlite3
conn = sqlite3.connect('my_dict_db.db', check_same_thread=False)
c = conn.cursor()
app = Flask(__name__)


@app.route("/home")
def index():
    return render_template('home.html')


@app.route("/home", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        var = request.form['name'].lower()
        corr = c.execute("SELECT * FROM my_dict_db_table where eng_word=='%s'" % var)
        data = corr.fetchall()
        return render_template('home.html', rows=data)


@app.route("/")
@app.route("/all_word")
def another():
    corr = c.execute("SELECT * FROM my_dict_db_table order by eng_word")
    data = corr.fetchall()
    return render_template('home.html', rows=data)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/a_to_e")
def a_to_e():
    corr = c.execute("SELECT * FROM my_dict_db_table where eng_word like 'a%' or eng_word like 'b%' "
                     "or eng_word like 'c%' or eng_word like 'd%' or eng_word like 'e%' order by eng_word")
    data = corr.fetchall()
    return render_template('home.html', rows=data)


@app.route("/f_to_j")
def f_to_j():
    corr = c.execute("SELECT * FROM my_dict_db_table where eng_word like 'f%' or eng_word like 'g%' "
                     "or eng_word like 'h%' or eng_word like 'i%' or eng_word like 'j%' order by eng_word")
    data = corr.fetchall()
    return render_template('home.html', rows=data)


@app.route("/k_to_o")
def k_to_o():
    corr = c.execute("SELECT * FROM my_dict_db_table where eng_word like 'k%' or eng_word like 'l%' "
                     "or eng_word like 'm%' or eng_word like 'n%' or eng_word like 'o%' order by eng_word")
    data = corr.fetchall()
    return render_template('home.html', rows=data)


@app.route("/p_to_t")
def p_to_t():
    corr = c.execute("SELECT * FROM my_dict_db_table where eng_word like 'p%' or eng_word like 'q%' "
                     "or eng_word like 'r%' or eng_word like 's%' or eng_word like 't%' order by eng_word")
    data = corr.fetchall()
    return render_template('home.html', rows=data)


@app.route("/u_to_z")
def u_to_z():
    corr = c.execute("SELECT * FROM my_dict_db_table where eng_word like 'u%' or eng_word like 'v%' "
                     "or eng_word like 'w%' or eng_word like 'x%' or eng_word like 'y%' or eng_word like 'z%'"
                     "order by eng_word")
    data = corr.fetchall()
    return render_template('home.html', rows=data)


class Urls:
    def valid_url_1(self):
        response = requests.get(f'http://127.0.0.1:5000/')
        if response.ok:
            return response.text
        else:
            return 'Bad Request'


if __name__ == '__main__':
    app.run(debug=True)
