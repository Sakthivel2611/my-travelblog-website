from flask import Flask, render_template

app = Flask(__name__)

# Sample data - you would replace this with your own data
travel_posts = [
    {  
       
        "title": "My Amazing Trip to Paris",
        
        "content": "I visited the Eiffel Tower and enjoyed the delicious French cuisine.Paris the City of Love and Lights, had always been a destination on my bucket list. The allure of its rich history, stunning architecture, and world-class cuisine drew me in, and finally, the day came when I set foot in this magical city.,Day 1: The Eiffel TowerMy trip began with a visit to the iconic Eiffel Tower. As I gazed up at its majestic iron structure, I was overcome with awe. The elevator ride to the top offered breathtaking panoramic views of Paris. It's true what they say - theres nothing quite like seeing the city from the Eiffel TowerThe Louvre Museum was my next stop. Home to thousands of art pieces, including the world-famous Mona Lisa, it was a cultural immersion like no other. I spent hours wandering through the grand halls, marveling at masterpieces from different eras."
    },
    {
        "title": "Exploring the Beaches of Bali",
        "content": "Bali's beaches are a paradise for surfers and sun lovers.Bali, the Island of the Gods, is renowned for its stunning beaches. Each beach on this Indonesian paradise has its unique charm and character. Here's a glimpse of some of the most popular and picturesque beaches in Bali."
        
    },
    {
        "title":"photos"
    },  
]

@app.route('/')
def home():
    return render_template('home.html', posts=travel_posts)


@app.route('/post/<int:index>')
def post(index):
    if 0 <= index < len(travel_posts):
        return render_template('post.html', post=travel_posts[index])
    return "Post not found."
    

if __name__ == '__main__':
    app.run(debug=True)