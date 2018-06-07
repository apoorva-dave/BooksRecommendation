import pandas as pd
import pprint as pp
import matplotlib.pyplot as plt
import numpy as np
users = pd.read_csv('C:/Users/Apoorva/PycharmProjects/BooksRecommenderSystem/BX-Users.csv',sep=';',error_bad_lines=False,encoding='latin-1',low_memory=False)
ratings = pd.read_csv('C:/Users/Apoorva/PycharmProjects/BooksRecommenderSystem/BX-Book-Ratings.csv',sep=';',error_bad_lines=False,encoding='latin-1',low_memory=False)
books= pd.read_csv('C:/Users/Apoorva/PycharmProjects/BooksRecommenderSystem/BX-Books.csv',sep=';',error_bad_lines=False,encoding='latin-1',low_memory=False)

counts1 = ratings['User-ID'].value_counts()
counts2 = ratings['Book-Rating'].value_counts()
ratings = ratings[ratings['User-ID'].isin(counts1[counts1>=100].index)]
ratings = ratings[ratings['Book-Rating'].isin(counts2[counts2>=100].index)]

# books_ratings = pd.merge(ratings,books,on='ISBN')
# pp.pprint(books_ratings.head())

print('User id as index, isbn as column and values as book rating')
ratings_pivot = ratings.pivot_table(index=['User-ID'],columns = ['ISBN'],values = 'Book-Rating')
pp.pprint(ratings_pivot.head())

average_ratings = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].mean())
average_ratings['rating-count'] = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].count())

myRatings = pd.DataFrame(ratings_pivot.loc['0'].dropna())
print(myRatings.head())

book_id_user = []
for row,index in myRatings.iterrows():
    book_id_user.append(row)
print('Book IDs read by user')
print(book_id_user)

print('Finding similarity between books rated by user 0 and other books')
user_matrix = []
similar_book_ids = []
for i in range(len(book_id_user)):
    users_col = ratings_pivot[book_id_user[i]]
    similarBooks = ratings_pivot.corrwith(users_col)
    similarBooks = similarBooks.dropna()
    similarBooksdf = pd.DataFrame(similarBooks, columns=['Similarity'])
    similarBooks_summary = similarBooksdf.join(average_ratings['rating-count'])
    pp.pprint(similarBooks_summary)
    similarBooks_summary = similarBooks_summary[similarBooks_summary['rating-count'] >= 300].sort_values('Similarity', ascending=False)
    print('Similarity scores')
    pp.pprint(similarBooks_summary.head())
    similarBooks_summary = similarBooks_summary.head()
    for row,index in similarBooks_summary.iterrows():
        similar_book_ids.append(row)

# print(similar_book_ids)
print('Books similar to books rated by user 0 are')
similar_book_ids = list(set(similar_book_ids))
# print(similar_book_ids)
most_similar_books = pd.DataFrame(similar_book_ids,index=np.arange(len(similar_book_ids)), columns=['ISBN'])
most_similar_books_titles = pd.merge(books, most_similar_books, on='ISBN')
pp.pprint(most_similar_books_titles)

