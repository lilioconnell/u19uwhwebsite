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


@app.route('/campaign', methods=["GET", "POST"])
def campaign():
    sql = """ select camps.camp_id, camps.camp_cost, camps.camp_location, camps.camp_date
        from camps """
    result = run_search_query_tuples(sql, (), db_path, True)
    print(result)
    return render_template("campaign.html", camps=result)

def register():
    msg = ''
    f = request.form
    if request.method == 'POST' and 'email' in request.form and 'billet' in request.form and 'billet_number' in request.form and 'other' in request.form:
        values_tuple = (f['email'], f['billet'], f['billet_number'], f['other'])
        sql = """INSERT INTO register(email, billet, billet_number, other) VALUES (?, ?, ?, ?)"""
        result = run_commit_query(sql, values_tuple, db_path)
        return redirect(url_for('campaign'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('campaign.html', msg = msg)



@app.route('/add_camp', methods=["GET", "POST"])
def add_camp():
    # collect data from the web address
    data = request.args
    required_keys = ['id', 'task']
    for k in required_keys:
        if k not in data.keys():
            message = "Do not know what to do with create read update on news (key not present)"
            return render_template('error.html', message=message)
    # have an id and a task key
    if request.method == "GET":
        if data['task'] == 'add':
            temp = {'location': 'Test Location', 'date': 'Test Date', 'cost': 'Test Cost'}
            temp = {}
            return render_template("add_camp.html",
                                   id=0,
                                   task=data['task'],
                                   **temp)
        else:
            message = "Unrecognised task coming from news page"
            return render_template('error.html', message=message)
    elif request.method == "POST":
        # collected form information
        f = request.form

        if data['task'] == 'add':
            # add the new entry to the database
            # member is fixed for now
            sql = """insert into camps(camp_location, camp_date, camp_cost)
                    values(?,?, ?)"""
            values_tuple = (f['camp_location'], f['camp_date'], f['camp_cost'])
            result = run_commit_query(sql, values_tuple, db_path)
            return redirect(url_for('campaign'))
        else:
            message = "unrecognized task coming from news submission"
            return render_template('error.html', message=message)



@app.route('/halloffame')
def halloffame():
    # query for page
    sql = """ select halloffame.hof_id, halloffame.name, halloffame.description, halloffame.socials, halloffame.headshot
        from halloffame """
    result = run_search_query_tuples(sql, (), db_path, True)
    print(result)
    return render_template("halloffame.html", halloffame=result)

@app.route('/hof_cud', methods=["GET", "POST"])
def hof_cud():
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
            sql = "delete from halloffame where hof_id = ?"
            values_tuple = (data['id'],)
            result = run_commit_query(sql, values_tuple, db_path)
            return redirect(url_for('halloffame'))
        elif data['task'] == 'update':
            sql = """ select name, description, socials, headshot from halloffame where hof_id=?"""
            values_tuple = (data['id'],)
            result = run_search_query_tuples(sql, values_tuple, db_path, True)
            result = result[0]
            return render_template("hof_cud.html",
                                   **result,
                                   id=data['id'],
                                   task=data['task'])
        elif data['task'] == 'add':
            temp = {'title': 'Test Title', 'content': 'Test Content'}
            temp = {}
            return render_template("hof_cud.html",
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
            sql = """insert into halloffame(name, description, socials, headshot)
                    values(?,?, ?, ?)"""
            values_tuple = (f['name'], f['description'], f['socials'], f['headshot'])
            result = run_commit_query(sql, values_tuple, db_path)
            return redirect(url_for('halloffame'))
        elif data['task'] == 'update':
            sql = """update halloffame set name=?, description=?, socials=?, headshot=? where hof_id=?"""
            values_tuple = (f['name'], f['description'], f['socials'], f['headshot'], data['id'])
            result = run_commit_query(sql, values_tuple, db_path)
            return redirect(url_for('halloffame'))
        else:
            message = "unrecognized task coming from news submission"
            return render_template('error.html', message=message)


@app.route('/training')
def training():
    sql = """ select training.cardio, training.pool, training.strength, training.intervals, training.games 
        from training """
    result = run_search_query_tuples(sql, (), db_path, True)
    print(result)
    return render_template("training.html",training=result)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    msg = ''
    f = request.form
    print(f)
    if request.method == 'POST' and 'first' in request.form and 'last' in request.form and 'phone' in request.form  and 'email' in request.form and 'enquiry' in request.form:
        values_tuple = (f['first'], f['last'], f['phone'], f['email'], f['enquiry'])
        sql = """INSERT INTO contact(first, last, phone, email, enquiry) VALUES (?, ?, ?, ?, ?)"""
        result = run_commit_query(sql, values_tuple, db_path)
        return redirect(url_for('contact'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('contact.html', msg = msg)



@app.route('/blog')
def blog():
    # query for page
    sql = """ select blog.blog_id, blog.title, blog.content, blog.date, blog.picture, member.name
        from blog
        join member on blog.member_id= member.member_id
        order by blog.date desc;
        """
    result_blog = run_search_query_tuples(sql, (), db_path, True)
    print(result_blog)

    sql = """select comments.comment_id, comments.content, comments.date, member.name
    from comments
    join member on comments.member_id = member.member_id
    order by comments.date desc;
    """
    result_comment = run_search_query_tuples(sql, (), db_path, True)
    print(result_comment)
    return render_template("blog.html", blog=result_blog, comments=result_comment)



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

@app.route('/comment_cud', methods=["POST"])
def comment_cud():
    if request.method == "POST":
        f = request.form
        print(f)
        print(f['comment'])
        sql = """ insert into comments(content, date, member_id, blog_id) values (?, datetime('now', 'localtime'),?,?)"""
        values_tuple = (f['comment'], session['member_id'], f['blog_id'])
        result = run_commit_query(sql, values_tuple, db_path)
        return redirect(url_for('blog'))
@app.route('/login', methods=["GET", "POST"])
def login():
    print(session)
    error = "Your credentials are not recognised"
    if request.method == "GET":
        return render_template("login.html")
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
                return render_template("login.html", error=error)
        else:
            return render_template("login.html", error=error)

@app.route('/signup', methods =['GET', 'POST'])
def signup():
    msg = ''
    f = request.form
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form and 'authorisation' in request.form:
        values_tuple = (f['name'], f['password'], f['email'], f['authorisation'])
        sql = "INSERT INTO member (name, password, email, authorisation) VALUES (?, ?, ?, ?)"
        result = run_commit_query(sql, values_tuple, db_path)
        return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('signup.html', msg = msg)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(port=8000,debug=True)
