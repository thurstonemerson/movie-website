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

