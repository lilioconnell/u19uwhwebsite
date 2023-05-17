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


if __name__ == "__main__":
    db_path = 'data/pasta_db.sqlite'
    get_blog(db_path)