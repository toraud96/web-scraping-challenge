from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
import scrape_mars

# #################################################
# # Setup Dictionary of Mars_data
# #################################################


#################################################
# Flask Routes
#################################################
# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_data)

# @app.route('/')
# def index():
#
#     # Store the entire mars news collection in a list
#     mars = list(db.nasa.find(news_title, news_p))
#     print(mars)
#
#     # Return the template with the news passed in
#     return render_template('index.html', mars=mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

