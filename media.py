'''
Created on 31/07/2015

@author: thurstonemerson
'''

def get_latest_releases():

    '''Retrieve movies from TMDb API that are now playing in theatres'''
    
    TMDb_connect = urllib.urlopen('https://api.themoviedb.org/3/movie/now_playing?api_key=23d81fdf84638b37ab9f8d898c12243c')
    movie_json = json.loads(TMDb_connect.read())
    TMDb_connect.close()
    
    movies = []

    for result in movie_json['results']:           
        print "{0}, {1}, {2}, {3}, {4}, {5}".format(result['id'], result['title'], result['overview'], result['poster_path'], result['release_date'], result['vote_average']))
        
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

