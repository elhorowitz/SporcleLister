import urllib2, csv
from BeautifulSoup import BeautifulSoup

# Here is the method that takes the games in Sporcle.com and puts them into a list
def process_apa_page(url):

    # Get the page in question (http://www.sporcle.com/games/category/)
    script = urllib2.urlopen(url).read()

    # Parse it with BeautifulSoup
    tree = BeautifulSoup(script)
    # print tree

    # initialize the lists to be used
    fullgames = []
    allgames = []
    categories = []

    # Search for games
    for post in tree.findAll('div', 'gameinfo'):
        gameName = ''
        catName = ''
        for game in post.findAll('a'):
            if "/category/" in '%s' %game:
                catName = '%s' %game
            else:
                gameName = '%s' %game
        
        fullgames.append([gameName, catName])     # This is as far as python will let me go in the tree, so we'll extract the titles of the games by hand   
        
    # Extract the title of the games
    for object in fullgames:
        
        # Separate the '<a href="...php">' from the title
        object[0] = object[0].partition('">')
        object[1] = object[1].partition('">')
        # print object
        
        # Only take the title part of the separation
        gameTitle = object[0][2]
        catTitle = object[1][2]
        
        # Separate the '</a>' from the text
        gameTitle = gameTitle.rpartition('</a>')
        catTitle = catTitle.rpartition('</a>')
        # print [gameTitle[0],catTitle[0]]
        
        # Add the game title to the list of games
        allgames.append([gameTitle[0], catTitle[0]])

    return allgames

# Start the extraction process
games = process_apa_page('http://www.sporcle.com')

# Display the results
for game in games:
    print game[0]+" is a "+game[1]+" game!"