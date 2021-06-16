# dictionaries help us store complicated data, which is not single valued like a number or a string
book = {
    'title': "How to be awesome",
    'author': "john doe",
    'isbn': "1234-23-15-12-3",
    'date_published': "23-21-2010",
    'year': 2010
}
# access
book_title = book['title']
print(book_title)
# update
book['title'] = "2020 what went wrong"
print(book["title"])
# get all the keys in this dictionary
keys = book.keys()
print(keys)
# YOU CAN COMBINE ARRAYS WITH DICTIONARIES
books = [{
    'title': "How to be awesome",
    'author': "john doe",
    'isbn': "1234-23-15-12-3",
    'date_published': "23-21-2010",
    'year': 2010
},
    {
    'title': "How to be cool",
    'author': "Alice",
    'isbn': "1111-23-15-12-3",
    'date_published': "02-01-2018",
    'year': 2018
},
]

# now lets look at something more complex
# excercise
bags = {
    'books': [{
        'title': "How to be awesome",
        'author': "john doe",
        'isbn': "1234-23-15-12-3",
        'date_published': "23-21-2010",
        'year': 2010
    }, {
        'title': "How to be cool",
        'author': "Alice",
        'isbn': "1111-23-15-12-3",
        'date_published': "02-01-2018",
        'year': 2018
    }
    ],
    'stationaries': [
        {
            "pencils": 2,
            "ball_pens": 5
        }
    ],

}
print(bags)
