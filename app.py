import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_book'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster-mknew.mongodb.net/recipe_book?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", page_title="Recipes", recipes=mongo.db.recipes.find(), cuisines=mongo.db.cuisines.find()
    )


@app.route('/playaround')
def playaround():

    return render_template("playaround.html", page_title="Playaround", recipes=mongo.db.recipes.find(), cuisines=mongo.db.cuisines.find())


@app.route('/add_recipe')
def add_recipe():
    the_recipe = mongo.db.recipes.find()
    all_cuisines = mongo.db.cuisines.find()
    return render_template('addrecipe.html', page_title="Add Recipe", recipe=the_recipe, cuisines=all_cuisines)   


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    input_data = request.form.to_dict()
    recipe_ingredients = input_data["recipe_ingredients"].split("\n")
    the_recipe = recipes.insert_one(
        {
         "recipe_name": input_data["recipe_name"],
         "recipe_description": input_data["recipe_description"],
         "recipe_cost": input_data["recipe_cost"],
         "recipe_time": input_data["recipe_time"],
         'is_healthy':request.form.get('is_healthy'),
         'is_vegetarian':request.form.get('is_vegetarian'),
         "recipe_cuisine_image": input_data["recipe_cuisine_image"],
         "ingredients": recipe_ingredients
        }
    )
    return redirect(url_for('get_recipes', recipe_id=the_recipe.inserted_id))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find()
    return render_template('editrecipe.html', page_title="Edit Recipe", recipe=the_recipe, cuisines=all_cuisines)




@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_cost': request.form.get('recipe_cost'),
        'recipe_time':request.form.get('recipe_time'),
        'is_healthy':request.form.get('is_healthy'),
        'is_vegetarian':request.form.get('is_vegetarian'),
        'recipe_cuisine_image':request.form.get('recipe_cuisine_image')



    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))








if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)