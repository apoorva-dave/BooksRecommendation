# BooksRecommendation
====================

## Introduction
BooksRecommendation involves suggesting books to users depending on their past interest. Here I have used Item based collaborative filtering to identify books similar to a particular book.

## Objective

  1. Find books similar to a particular book.
  2. Building a full blown book recommendation system suggesting users their books of itnerest.
  3. Plots to visualize most rated books, most active age group etc.

## Dataset
The dataset used here is Book-Crossings which is a book-ratings dataset collected by Cai-Nicolas Ziegler. There are 1.1 million ratings of 270,000 books by 90,000 users. The ratings are on a scale from 1 to 10. The dataset can be downloaded from http://www2.informatik.uni-freiburg.de/~cziegler/BX/

There are 3 csv files in the dataset :

  1. BX-Books : This gives the book titles, ISBN and some other details about book.
  2. BX-Users : This gives the user-id, location and their age who rated the books.
  3. BX-Book-Ratings : This gives the ISBN of books, ratings for each book and user id who rated that particular book.

## Dependencies
  1. Python
  2. Pandas
  3. Matplotlib
  4. Numpy

## Setup

File similarBooks.py is mainly focussed on finding books similar to a particular book. Here I am finding similarity of 'The Lovely Bones: A Novel' 2nd most rated book with other books. 
The code can be extended to any book from dataset as per requirement. Some graph plots are made to get a clear gist of the dataset.

For building a full blown recommendation system, I have added a dummy test user with user id '0' who has rated different books. 
In file itembased_recommendation.py, we are finding correlation for each book rated by User 0 and recommending him books depending on his past history.

The original dataset can be downloaded from http://www2.informatik.uni-freiburg.de/~cziegler/BX/

In this repository you can find the updated Users2.csv and BX-Book-Ratings2.csv where User-ID '0' and books rated by him are added which is required for building the code itembased_recommendation.py
