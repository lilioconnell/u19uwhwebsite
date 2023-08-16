from db_function import run_search_query_tuples

def get_blog(db_path):
    sql = """select blog.title, blog.content, member.name
    from blog
    join member on blog.member_id = member.member_id
    """
    result = run_search_query_tuples(sql, (), db_path, True)


    for row in result:
        for k in row.keys():
            print(k)
            print(row[k])

def get_comments(db_path):
    sql = """ select blog.blog_id, blog.title, blog.content, blog.date, blog.picture, member.name
        from blog
        join member on blog.member_id= member.member_id
        order by blog.date desc;
        """
    result_blog = run_search_query_tuples(sql, (), db_path, True)

    sql = """select comments.comment_id, comments.content, comments.date, member.name,  blog.blog_id
    from comments
    join member on comments.member_id = member.member_id
    join blog on comments.blog_id = blog.blog_id
    order by comments.date desc;
    """
    result_comment = run_search_query_tuples(sql, (), db_path, True)

    for b in result_blog:
        print(b['title'])
        for c in result_comment:
            if c['blog_id']==b['blog_id']:
                print(c['content'])




if __name__ == "__main__":
    db_path = 'data/pasta_db.sqlite'
    #get_blog(db_path)
    get_comments(db_path)