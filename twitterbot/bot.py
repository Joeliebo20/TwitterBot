import tweepy as tw
import time
from datetime import datetime
from credentials import *
import random


random_num = random.randint(1, 20000)

list_of_ppl = ['Drake', 'Travis Scott', 'Scarlett Johansen', 'Iron Man', 'Guy Fieri', 'Davante Adams', 'Joe Biden', 'Donald Trump', 'Jeff Bezos', 'Tom Cruise', 'Saquon Barkley', 'Derek Jeter', 'Aaron Judge', 'Albert Einstein', 'Gandhi', 'Abraham Lincoln', 'Helen Keller',
    'J.K. Rowling', 'Queen Elizabeth', 'Billie Eilish', 'Winston Churchill', 'Bill Gates', 'Steve Jobs', 'Paul McCartney', 'Franklin D. Roosevelt', 'Thomas Edison', 'Alexander Graham Bell', 'Ludwig Beethoven', 'Oprah Winfrey', 'Vladimir Putin', 'Neil Armstrong', 'Barack Obama', 
    'Michael Jordan', 'Fidel Castro', 'Pablo Picasso', 'Leonardo DiCaprio', 'Amelia Earhart', 'Michael Jackson', 'Cleopatra', 'Roger Federer', 'Sam from ICarly', 'Tiger Woods', 'Margaret Thatcher', 'George Clooney', 'Rick Sanchez', 'Beyonce', 'Tom Hanks', 'Ellen DeGeneres', 'George W. Bush',
    'Morgan Freeman', 'Sandra Bullock', 'Elton John', 'Snoop Dogg', 'Taylor Swift', 'Will Ferrell', 'Kanye West', 'Will Smith', 'Justin Bieber', 'Mariah Carey', 'Jimmy Fallon', 'Brad Pitt', 'Denzel Washington', 'Sylvester Stallone', 'Dwayne Johnson', 'Samuel L. Jackson', 'Jackie Chan', 'Jamie Foxx', 
    'Mick Jagger', 'Ice Cube', 'Lebron James', 'Kevin Durant', 'Steph Curry', 'Daniel Jones', 'New York Giants Wide Receiver Kenny Golladay', 'Lionel Ritchie', 'Ryan Lieberman', 'Kareem Abdul-Jabbar', 'Mike Wazowski', 'Marilyn Monroe', 'Kevin Hart', 'Alexander the Great', 'Spongebob Squarepants', 'Patrick Star', 
    'James Bond', 'Simon Cowell', 'Howie Mandell', 'Aaron Rodgers', 'Rapper Lil Baby', 'Gordon Ramsey', 'Baseball Player Mike Trout', 'NBA Superstar Luka Doncic', 'Giannis Antetokounmpo', 'Tall Guy Yao Ming', 'Robotics Professor', 'Zach from Zach and Cody', 'J. Cole', 'Kendrick Lamar', 'Upcoming Rapper Eminem',
    'World Chess Champion Magnus Carlsen', 'Superman', 'Batman', 'Ryan Reynolds', 'New York Knicks Star Player RJ Barrett', 'Scientific Genius Galileo Galilei', 'Copernicus', 'Greek Philosopher Plato', 'Legendary Philosopher and Singer/Songwriter Confucious', 'Dale Earnheardt Jr.', 'Dave Portnoy', 'Charli Damelio']

list_rand = random.randint(0, len(list_of_ppl) - 1)
list_rand2 = random.randint(0, len(list_of_ppl) - 1)

actions = ['watched the baseball game', 'is currently eating ice cream', f'would beat up {list_of_ppl[list_rand2]}', 'walked to the park today', 'attempted to destroy the world today', 'sang a terrible song early this afternoon', 'was casted to play the main character in the brand new hit movie The Emoji Movie 2', 'hates IPhones', 
    'has decided to become the new Queen of England', 'played Tennis and failed miserably', 'went to the moon', 'stole the Mona Lisa', 'aproves this message', 'once played flute', 'watched the new House of Dragon episode and said quote "a 10/10"', 'now owns the New York Yankees', f'hired Saul Goodman as their lawyer in a trial against {list_of_ppl[list_rand2]}', 
    f'fought bravely against opposing commander {list_of_ppl[list_rand2]} at the battle of London', 'sang the Gettysburg Address at their talent show', 'once said "Alcohol! Because no great story started with someone eating a salad."', 'wants to be me so bad', 'has been hired to play Peter Griffin in Family Guy 2', 'parted the Red Sea', 'knows how to do stuff', 
    f'is actually blood-related to {list_of_ppl[list_rand2]}', 'once put a pair of sunglasses on a pineapple', ': destroyer of worlds', 'just bought the NBA and is now its rightful owner', 'wants to buy a Jimmy Johns', 'earned extra credit in class by presenting first', 'ate leaves from a tree when they were a child', 'ate shellfish and cried', 
    'is the greatest trumpet player on planet Earth', 'swung and missed', 'thought they did something of importance today', 'tweeted out "roses are red, violets are blue"', 'won a track race when they were 7', 'is currently listening to Starships by Nicki Minaj', 'went to the mall', 'traveled back in time', f'lost in a staring contest to {list_of_ppl[list_rand]}']    
action_rand = random.randint(0, len(actions) - 1)

tweet_list = ['What up world', f'{list_of_ppl[list_rand]} wants to rediscover gravity', 'Does anyone know how to make a grilled cheese sandwich','Tweeting', 'Drake is much better than Travis Scott', 'Travis Scott is much better than Drake', 'Go outside', 'Do you prefer hamburger or cheeseburger', ':)', ':(', 
    'My test was hard', 'Will he be able to catch the train??', 'At a high school', 'I have a bad headache', f'{list_of_ppl[list_rand]} is NOT allergic to seafood', 'The NFL is rigged', 'The MLB is boring to watch', 'I need food', 'Moes is better than Chipotle', "I can't speak English at all", 'Blah blah random tweet', 
    'IPhone 17', "You know what's up", 'No', 'Yes', 'Oklahoma City is such a cool city name', 'Mcdonalds', 'Something opinonated', 'New show idea: Family guys', 'New show idea: Family girl', 'Ice cream is tasty', f'You have {random_num} new messages', f'There are {random_num} pizza huts in the world', 'The number of dominos stores is dramatically dropping', 
    'Cookie dough is the best flavor', 'Bereal is an app', 'Chocolate milk', 'Nesquick is trash', 'NASA just found out about space', 'How am I coming up with all of these topics', f'{list_of_ppl[list_rand2]}', f'Just saw {list_of_ppl[list_rand2]} eating pigs in a blanket', 'Does anyone actually enjoy wearing jeans?', 
    f'Hit singer/songwriter {list_of_ppl[list_rand2]} was caught drinking Pepsi Zero', 'Nathaniel Hackett is the worst coach in the NFL', 'Bob Costas is the perfect announcer to listen to if you want to go to sleep', 'Carrots and Broccoli > most vegetables', 'Opinonated tweet', 'Non-opinonated tweet', 'I remember the first time I cut onions', 
    'cheesburger not in paradise', 'strawberry banana smoothie','The opposite of opposite is positive', 'benevolent is an awesome word and should be used more', 'racecar is racecar backwards', 'average twitter bot tweet', 'I like mine with lettuce and tomato', 'Mmmmm im hungry give me tide pods', 'The fantasy football waiver wire this week is looking scarce', 
    'Please help me with my essay', 'LinkedIn', 'I refuse to believe the world has become a place where one cannot "skip class".', 'Seriously? 9 + 10 is not 21', 'AYYYYY MACARENA', 'This is literally a twitter bot', 'Fabian Moreau is better than your favorite corner', 'Google it', 'Amazonian Jungle or Amazon the company', 'This is not an advertisement for jelly beans', 
    'Steve Harvey the type of dude to believe in Manifest Destiny', 'Napolean Bonaparte was such a bottom tier IRL villain', 'We are going on a trip in our favorite rocket ship', 'I am going to make salmon for dinner tonight', 'Better Call Saul', 'Henny Cans are a good beer', 'Vodka or Lemonade? - Russian guy, probably', 'Scrabble is an ELITE board game', 'Beans suck so bad',
    'Alexander Graham Bell did not invent anything of importance', 'Canadiens are pretty cool', 'Hockey is a good sport I will not lie', 'Why do I speak in the first person if I am literally a bot', 'Gmail is the king of emails', 'Androids suck', 'Controversial Opinion', 'Literally what is the point of Non-alcoholic beer', 'Put the quarter in the Aldis shopping cart', 'Hard or soft pillows',
    'Charging stations are just gas stations for irregular cars', 'https://somewebsite.com', 'Ninjas are something that I thought would be wayyy more prominent in my life', 'Miller Lite underrated (I am literally a robot)', 'Beer ball?', 'Racketball is fake tennis', 'Uno reverse card', f'{list_of_ppl[list_rand]} seems like a great chess player']



def setup():
    # sets up the twitter client
    clnt = tw.Client(bearer, api_key, api_key_secret, access_token, access_token_secret)
    api = tw.API(clnt)
    return clnt

def generate_tweet():
    # this function generates tweets randomly based on the names and actions provided above
    tweet = list_of_ppl[list_rand] + " " + actions[action_rand]
    return tweet

def tweet(client): 
    # this function created a random tweet and tweets it out.
    rand = random.randint(0, len(tweet_list)-1)
    rand2 = random.randint(0, 1)
    if rand2 == 0:
        tweet = tweet_list[rand]
    else:
        tweet = generate_tweet()
    try:
        client.create_tweet(text=tweet)
        print(f"tweeted '{tweet}'")
    except Exception as err:
        print("already tweeted this!")
    time.sleep(86400)
    

def main():
    client = setup()
    while True:
        time = datetime.now()
        day = time.day
        if day % 1 == 0:
            # tweets every day
            tweet(client)

main()
