'''
Created on 31/07/2015

This module can be used to retrieve/display in a webpage the latest movie releases
now playing in theatres. At the moment only the first 20 results are displayed.
Each movie has associated details such as overview, average
popularity vote and release date. The movie trailer can be viewed by clicking on the
poster or 'view trailer' button.

This module  utilises the TMDb API, this requires attribution in the about section 
(This product uses the TMDb API but is not endorsed or certified by TMDb)
API key is 23d81fdf84638b37ab9f8d898c12243c

At the moment this program is tightly bound to the TMDb API so some more steps are necessary
to remove this dependence (in case we should require using a different API in future)

@author: thurstonemerson
'''
import json
import urllib
import webbrowser
import os

# Make two columns of movie tiles for medium and large devices, tablet and mobile devices will stack tiles
movie_tile_row_header = u'''
        <div class="row form-group">
        '''
movie_tile_row_end = u'''
        </div> <!-- /.div row-->
        '''
movie_tile_row_content = u'''
            <div id="movie-tile" class="col-md-6">
                <div class="media-left">
                    <a href="#" class="view-trailer" data-movie-id="{movie_id}" data-toggle="modal" data-target="#trailer">
                        <img class="media-object" src="{poster_image_url}" alt="...">
                    </a>
                 </div><!-- /.div media-left-->
                 <div class="media-body">
                     <h4 class="media-heading">{movie_title}</h4>
                     <h6 class="media-heading">{vote_average}
                         <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
                         <div class="release-date">{release_date}</div>
                     </h6>
                     <p>{overview}</p>
                     <button type="button" class="btn btn-default view-trailer" data-movie-id="{movie_id}" data-toggle="modal" data-target="#trailer">View trailer &raquo;</button>
                </div><!-- /.div media-body-->
             </div><!-- /.div col-md-6-->
'''


def create_movie_tile_row(movie1, movie2):
    '''Creates a row in a bootstrap grid with two columns containing a movie tile each'''

    content = movie_tile_row_header
    content += movie_tile_row_content.format(movie_title=movie1.title,
                                         poster_image_url=movie1.poster_image_url,
                                         movie_id=movie1.movie_id,
                                         overview=movie1.overview,
                                         vote_average=movie1.vote_average,
                                         release_date=movie1.release_date)
    content += movie_tile_row_content.format(movie_title=movie2.title,
                                         poster_image_url=movie2.poster_image_url,
                                         movie_id=movie2.movie_id,
                                         overview=movie2.overview,
                                         vote_average=movie2.vote_average,
                                         release_date=movie2.release_date)
    content += movie_tile_row_end
    
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
        
        
