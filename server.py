from flask import Flask, render_template, request, redirect, url_for
from db_function import run_search_query_tuples
from datetime import datetime

app = Flask(__name__)
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
    # query for page
    sql = """ select blog.blog_id, blog.title, blog.content, blog.date, member.name
    from blog
    join member on blog.member_id= member.member_id
    order by blog.date desc;
    """
    result = run_search_query_tuples(sql, (), db_path, True)
    print(result)
    return render_template("training.html", blog=result)

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)