import harpiya

def paginate(doctype, page=0, conditions=" ", paginate_by=6):
    prev, next, search = 0, 0, False
    query = f"""SELECT name, property_name, status, address, grand_total,
                image FROM `tab{doctype}` {conditions} ORDER BY creation DESC """

    if(page):
        page = int(page)
        products = harpiya.db.sql(query+f"""LIMIT {(page*paginate_by)-paginate_by}, {paginate_by};""", as_dict=True)
        next_set = harpiya.db.sql(query+f"""LIMIT {page*paginate_by}, {paginate_by};""", as_dict=True)
        if(next_set):
            prev, next = page-1, page+1
        else:
            prev, next = page-1, 0
    else:
        count = harpiya.db.sql(f"""SELECT COUNT(name) as count FROM `tab{doctype}` {conditions};""", as_dict=True)[0].count
        if(count>paginate_by):
            prev, next = 0, 2
        else:
            pass
        properties = harpiya.db.sql(query+f"""LIMIT {paginate_by};""", as_dict=True)

    if(conditions):
        search=True
    return {
        'products': products,
        'prev': prev,
        'next': next,
        'search':search,
    }