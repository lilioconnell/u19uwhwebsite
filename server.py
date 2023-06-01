from flask import Flask, render_template, request, redirect, url_for, session
from db_function import run_search_query_tuples, run_commit_query
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ertyuiop"
db_path = 'data/pasta_db.sqlite'


@app.template_filter()
def date(sqlite_dt):
    # create a date object
    x = datetime.strptime(sqlite_dt, '%Y-%m-%d %H:%M:%S')
    return x.strftime('%a %d %b %y %H:%M')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/campaign')
def campaign():
    return render_template("campaign.html")


@app.route('/halloffame')
def halloffame():
    return render_template("halloffame.html")


@app.route('/training')
def training():
    return render_template("training.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/blog')
def blog():
    # query for page
    sql = """ select blog.blog_id, blog.title, blog.content, blog.date, member.name
        from blog
        join member on blog.member_id= member.member_id
        order by blog.date desc;
        """
    result = run_search_query_tuples(sql, (), db_path, True)
    print(result)
    return render_template("blog.html", blog=result)


@app.route('/blog_cud', methods=["GET", "POST"])
def blog_cud():
    # collect data from the web address
    data = request.args
    required_keys = ['id', 'task']
    for k in required_keys:
        if k not in data.keys():
            message = "Do not know what to do with create read update on news (key not present)"
            return render_template('error.html', message=message)
    # have an id and a task key
    if request.method == "GET":
        if data['task'] == 'delete':
            sql = "delete from blog where blog_id = ?"
            values_tuple = (data['id'],)
            result = run_commit_query(sql, values_tuple, db_path)
            return redirect(url_for('blog'))
        elif data['task'] == 'update':
            sql = """ select title, content from blog where blog_id=?"""
            values_tuple = (data['id'],)
            result = run_search_query_tuples(sql, values_tuple, db_path, True)
            result = result[0]
            return render_template("blog_cud.html",
                                   **result,
                                   id=data['id'],
                                   task=data['task'])
        elif data['task'] == 'add':
            temp = {'title': 'Test Title', 'content': 'Test Content'}
            temp = {}
            return render_template("blog_cud.html",
                                   id=0,
                                   task=data['task'],
                                   **temp)
        else:
            message = "Unrecognised task coming from news page"
            return render_template('error.html', message=message)
    elif request.method == "POST":
        # collected form information
        f = request.form
        # print(f)
        if data['task'] == 'add':
            # add the new entry to the database
            # member is fixed for now
            sql = """insert into blog(title,content,date,member_id)
                    values(?,?, datetime('now', 'localtime'), ?)"""
            values_tuple = (f['title'], f['content'], session['member_id'])
            result = run_commit_query(sql, values_tuple, db_path)
            return redirect(url_for('blog'))
        elif data['task'] == 'update':
            sql = """update blog set title=?, content=?, date=datetime('now', 'localtime') where blog_id=?"""
            values_tuple = (f['title'], f['content'], data['id'])
            result = run_commit_query(sql, values_tuple, db_path)
            return redirect(url_for('blog'))
        else:
            message = "unrecognized task coming from news submission"
            return render_template('error.html', message=message)



@app.route('/login', methods=["GET", "POST"])
def login():
    print(session)
    error = "Your credentials are not recognised"
    if request.method == "GET":
        return render_template("login.html", email='mmurdoch@yahoo.com', password="temp")
    elif request.method == "POST":
        f = request.form
        print(f)
        sql = """ select name, password, authorisation, member_id from member where email = ?"""
        values_tuple = (f['email'],)
        result = run_search_query_tuples(sql, values_tuple, db_path, True)
        if result:
            result = result[0]
            if result['password'] == f['password']:
                # start a session
                session['name'] = result['name']
                session['authorisation'] = result['authorisation']
                session['member_id'] = result['member_id']
                return redirect(url_for('index'))
            else:
                return render_template("login.html", email='rbrosn@gmail.com', password="temp", error=error)
        else:
            return render_template("login.html", email='rbrosn@gmail.com', password="temp", error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
