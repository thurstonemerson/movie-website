'''
Created on 31/07/2015

Retrieves a list of the latest movie releases and displays them on a webpage


@author: thurstonemerson
'''
import sys
import media

def main():

    movies = media.get_latest_releases()
    
    pass

if __name__ == '__main__':
    sys.exit(main())
