import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pprint as pp
books = pd.read_csv('C:/Users/Apoorva/PycharmProjects/BooksRecommenderSystem/BX-Books.csv',sep=';',error_bad_lines=False,encoding='latin-1')
users = pd.read_csv('C:/Users/Apoorva/PycharmProjects/BooksRecommenderSystem/BX-Users.csv',sep=';',error_bad_lines=False,encoding='latin-1')
ratings = pd.read_csv('C:/Users/Apoorva/PycharmProjects/BooksRecommenderSystem/BX-Book-Ratings.csv',sep=';',error_bad_lines=False,encoding='latin-1')
books_columns = books.columns.values
users_columns = users.columns.values
ratings_columns = ratings.columns.values

ratings['Book-Rating'].value_counts(sort=False).plot(kind='bar')
plt.title('Count of Ratings')
plt.xlabel('Book-Rating')
plt.ylabel('Count')
plt.show()

users['Age'].hist(bins = [10,20,30,40,50,60,70,80,90])
plt.title('Most active Age group')
plt.xlabel('Age Group')
plt.ylabel('Ratings')
plt.show()

print('Locations from where ratings are made')
location = []
for index, row in users.iterrows():
    location.extend(row['Location'].split(','))
print(list(set(location)))

print('Most rated book..')
ratings_count = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].count())
ratings_count['count'] = ratings_count.sort_values('Book-Rating',ascending=False).head()
most_rated_books  = pd.DataFrame(['0971880107','0316666343','0385504209','0060928336','0312195516'],index=np.arange(5),columns=['ISBN'])
most_rated_books_titles = pd.merge(books,most_rated_books,on='ISBN')
pp.pprint(most_rated_books_titles)

average_ratings = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].mean())
# print(average_ratings.sort_values('Book-Rating',ascending=False).head())
average_ratings['rating-count'] = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].count())
print(average_ratings.sort_values('rating-count',ascending=False).head())

print('Showing book avg rating and no of ratings count are not related')

counts1 = ratings['User-ID'].value_counts()
counts2 = ratings['Book-Rating'].value_counts()
ratings = ratings[ratings['User-ID'].isin(counts1[counts1>=200].index)]
ratings = ratings[ratings['Book-Rating'].isin(counts2[counts2>=100].index)]
booksRatings = ratings.pivot_table(index='User-ID',columns='ISBN',values='Book-Rating')
pp.pprint(booksRatings.head())

print('Finding similarity of 2nd most rated book 0316666343 The Lovely Bones: A Novel with other books')
# print('Users who rated lovely bones.')
userRating = booksRatings['0316666343']
# print(userRating)

similarBooks = booksRatings.corrwith(userRating)
similarBooks = similarBooks.dropna()
similarBooksdf = pd.DataFrame(similarBooks,columns=['Similarity'])
# print(similarBooksdf)
similarBooks_summary = similarBooksdf.join(average_ratings['rating-count'])
# print(similarBooks_summary)
similarBooks_summary = similarBooks_summary[similarBooks_summary['rating-count']>=300].sort_values('Similarity',ascending=False)
# pp.pprint(similarBooks_summary.head())

print('Printing books similar to lovely bones..')
most_similar_books  = pd.DataFrame(['0316666343','0312291639','0316601950','0446610038','0446672211'],index=np.arange(5),columns=['ISBN'])
most_similar_books_titles = pd.merge(books,most_similar_books,on='ISBN')
pp.pprint(most_similar_books_titles)
