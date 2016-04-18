# Movie Website

Movie Website is an application where you can view the details and trailers of movies that have been released in the last week. 
Details of a movie that you can view include an overview, average popularity vote and release date. The movie trailer can be viewed by 
clicking on the poster or 'view trailer' button. Movie data is refreshed daily.

## Environment

You'll need the following for your development environment:

- [Python] (http://www.python.org)
- [virtualenv] (https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv) (recommended)

## Local Installation

The following assumes you have all of the tools listed above installed.

1. Clone the project:

    ```
	$ git clone https://github.com/thurstonemerson/movie-website.git
	$ cd movie-website
    ```

1. Create and initialize virtualenv for the project:

    ```
	$ mkvirtualenv movie-website
    ```
    
1. Create and initialize virtualenv for the project:

    ```
	$ mkvirtualenv swiss-system-tournament
    ```

## Run the program

- Execute the following command to generate the html file:

    ```
 	$ python entertainment_center.py
     ```
 
- The file fresh_tomatoes.html will be generated and opened in the default browser.


### Known issues
- Only the first 20 movies released in the previous week are displayed.

## Disclaimer

This application uses the TMDb API to retrieve the movie data but is not endorsed or certified by TMDb.

## License

The MIT License (MIT)

Copyright (c) 2016 Thurston Emerson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

