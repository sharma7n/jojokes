# jojokes flask app
# serves up a random JoJo's Bizarre Adventure joke on each page load.

import os
from random import seed, choice

from flask import Flask, render_template, redirect, url_for

# app init
app = Flask(__name__)
seed()

# define the models
class Joke:
    
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline
        
    def __repr__(self):
        return 'Joke({}, {})'.format(self.setup, self.punchline)
    
jokes = [
    Joke("What is Joseph's favorite type of meat?", "Hamon iberico."),
    Joke("Did you hear what happened to Joseph's hand?", "He lost it in a Kars accident."),
    Joke("If Wham! were your personal butler, what would he say to you every morning?", "Awaken, my master."),
    Joke("What is Dio's favorite TV sitcom?", "Everyone loves WRYYYYmond."),
    Joke("What is Avdol's least favorite dessert?", "Vanilla ice cream."),
    Joke("What kind of flowers does Jotaro buy for his mom?", "Yare yare daisies."),
    Joke("What does Caeser have in common with soda?", "They both go flat when they run out of bubbles."),
    Joke("What's Dio's favorite children book?", "Where's Za Waldo."),
    Joke("Why did Avdul die?", "He swallowed a hol horse."),
    Joke("How did Kakyoin know The World's ability?", "It's simple: he just had a gut feeling."),
]

# define the views
@app.route("/")
def index():
    joke = choice(jokes)
    return render_template("index.html",
                          title="Home",
                          joke=joke)

# app exec
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
               
