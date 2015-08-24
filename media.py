'''
Created on 31/07/2015

@author: thurstonemerson
'''

import json
import urllib
import webbrowser
import os

def create_movie_tile_row(movie1, movie2):
    '''Creates a row in a bootstrap grid with two columns containing a movie tile each'''

    content = ""
    
    return content


def create_movie_tiles_content(movies):
    ''' Creates the HTML content for the bootstrap movie grid'''
    
    content = u''
    
    # Take movies in groups of two in order to create rows with two columns of movies
    for movie1, movie2 in zip(movies[0::2], movies[1::2]):
        content += create_movie_tile_row(movie1, movie2)
  
        
    return content

def open_movies_page(movies):
    '''This function opens main.html and appends the movie content'''
    
    main_file = open('index.html', 'r')
    
    #read the index page context and convert to unicode object
    main_page_content = unicode(main_file.read(), 'utf8')
    main_file.close()

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))
   
    # Output the file after encoding as unicode-encoded string object 
    output_file.write(rendered_content.encode('utf8'))
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
    

def get_latest_releases():

    '''Retrieve movies from TMDb API that are now playing in theatres'''
    
    TMDb_connect = urllib.urlopen('https://api.themoviedb.org/3/movie/now_playing?api_key=23d81fdf84638b37ab9f8d898c12243c')
    movie_json = json.loads(TMDb_connect.read())
    TMDb_connect.close()
    
    movies = []

    for result in movie_json['results']:           
        movie = Movie(result['id'], result['title'], result['overview'], result['poster_path'], result['release_date'], result['vote_average'])
        print movie.movie_id, movie.title.encode('utf8'), movie.poster_image_url.encode('utf8'), movie.release_date, movie.vote_average
        
        movies.append(movie)
        
    return movies

class Movie():
    '''
    Movie class holding the TMDb id, title, overview, poster image and release date
    '''

    def __init__(self, movie_id, title, overview, poster_image_url, release_date, vote_average):

        if title is not None:
            self.title = title
        else:
            self.title = "Unknown"
            
        self.movie_id = movie_id
        
        if overview is not None:
            self.overview = overview
        else:
            self.overview = "No overview supplied"
        
        if overview is not None:
            self.poster_image_url = 'https://image.tmdb.org/t/p/w185' + poster_image_url
        else:
            self.poster_image_url = ''
            
        self.release_date = release_date
        self.vote_average = vote_average
        self.trailer_youtube_url = "http://www.youtube.com"

