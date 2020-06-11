import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'recipe_book'
app.config['MONGO_URI'] = \
    'mongodb+srv://root:r00tUser@myfirstcluster-mknew.mongodb.net/recipe_book?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/')
def landing():
    """ Route for index/landing page
    """

    return render_template('landing.html', page_title='Primal Recipes')


@app.route('/get_recipes')
def get_recipes():
    """ Route for page with all recipes
    """

    return render_template('recipes.html', page_title='Primal Recipes',
                           recipes=mongo.db.recipes.find(),
                           cuisines=mongo.db.cuisines.find())


@app.route('/vegetarian')
def vegetarian():
    """ Route for page with all recipes where is_vegetarian = on (on = true/selected)
    """

    veggie_recipes = mongo.db.recipes.find({'is_vegetarian': 'on'})
    all_cuisines = mongo.db.cuisines.find()
    return render_template('recipes.html',
                           page_title='Vegetarian Recipes',
                           recipes=veggie_recipes,
                           cuisines=all_cuisines)


@app.route('/healthy')
def healthy():
    """ Route for page with all recipes where is_healthy = on (on = true/selected)
    """

    healthy_recipes = mongo.db.recipes.find({'is_healthy': 'on'})
    all_cuisines = mongo.db.cuisines.find()
    return render_template('recipes.html', page_title='Healthy Recipes'
                           , recipes=healthy_recipes,
                           cuisines=all_cuisines)


@app.route('/read_recipe/<recipe_id>')
def read_recipe(recipe_id):
    """ Route for recipe details page, this is where users will view each recipe. You can access the delete and edit_recipe buttons from this page
    """

    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('readrecipe.html', recipe=the_recipe,
                           page_title='Read Recipe')


@app.route('/add_recipe')
def add_recipe():
    """ Route to page with the add_recipe form
    """

    the_recipe = mongo.db.recipes.find()
    all_cuisines = mongo.db.cuisines.find()
    return render_template('addrecipe.html', page_title='Add Recipe',
                           recipe=the_recipe, cuisines=all_cuisines)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """ Inserts a recipe to the MongoDB database using the input_data from the add_recipe form. Uses front and back end validation
    """

    recipes = mongo.db.recipes
    the_recipe = mongo.db.recipes.find()
    all_cuisines = mongo.db.cuisines.find()
    input_data = request.form.to_dict()
    recipe_ingredients = input_data['recipe_ingredients'].split('\n')
    recipe_instructions = input_data['recipe_instructions'].split('\n')

    validation_errors = []
    name = request.form.get('recipe_name', '')
    description = request.form.get('recipe_description', '')
    time = request.form.get('recipe_time', '')
    ingredients = request.form.get('recipe_ingredients', '')
    instructions = request.form.get('recipe_instructions', '')

    # Validate the recipe name. It can not be empty or longer than 50 characters long.

    if len(name) == 0 or len(name) > 50:
        validation_errors.append('The title should not be empty or longer than 50 characters long.'
                                 )

    # Validate the recipe description. It can not be empty or longer than 185 characters long.

    if len(description) == 0 or len(description) > 500:
        validation_errors.append('The description should not be empty or longer than 500 characters long.'
                                 )

    # Validate the recipe time. It can not be empty or longer than 12 characters long (enough space for a 3 digit number and a unit of measurement).

    if len(time) == 0 or len(time) > 12:
        validation_errors.append('The recipe time should not be empty or longer than 12 characters long.'
                                 )

    # Validate the recipe ingredients. It can not be empty or longer than 1000 characters long.

    if len(ingredients) == 0 or len(ingredients) > 1000:
        validation_errors.append('The list of ingredients should not be empty or longer than 1000 characters long.'
                                 )

    # Validate the recipe instructions. It can not be empty or longer than 1500 characters long.

    if len(instructions) == 0 or len(instructions) > 1500:
        validation_errors.append('The list of instructions should not be empty or longer than 1500 characters long.'
                                 )

    # If no errors on validation, display error message.

    if len(validation_errors) > 0:
        error_string = '\n'.join(validation_errors)
        return render_template('addrecipe.html', page_title='Add Recipe'
                               , errors=error_string,
                               recipe=the_recipe, cuisines=all_cuisines)

    the_recipe = recipes.insert_one({
        'recipe_name': input_data['recipe_name'],
        'recipe_description': input_data['recipe_description'],
        'recipe_cost': input_data['recipe_cost'],
        'recipe_time': input_data['recipe_time'],
        'is_healthy': request.form.get('is_healthy'),
        'is_vegetarian': request.form.get('is_vegetarian'),
        'recipe_cuisine_image': input_data['recipe_cuisine_image'],
        'ingredients': recipe_ingredients,
        'instructions': recipe_instructions,
        })

    return redirect(url_for('read_recipe',
                    recipe_id=the_recipe.inserted_id))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """ Route to the same form as add_recipe form with the details of the recipe the user wishes to edit
    """

    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find()
    all_ingredients = [ingredient for ingredient in
                       the_recipe['ingredients']]
    all_instructions = [instruction for instruction in
                        the_recipe['instructions']]

    each_ingredient = '\n'.join(all_ingredients)
    each_instruction = '\n'.join(all_instructions)

    return render_template(
        'editrecipe.html',
        page_title='Edit Recipe',
        recipe=the_recipe,
        cuisines=all_cuisines,
        ingredients=each_ingredient,
        instructions=each_instruction,
        )


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    """ Updates the selected recipe with the information in the edit_recipe form. Uses front and back end validation
    """

    recipes = mongo.db.recipes
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find()
    input_data = request.form.to_dict()
    all_ingredients = input_data['ingredients'].split('\n')
    all_instructions = input_data['instructions'].split('\n')
    each_ingredient = '\n'.join(all_ingredients)
    each_instruction = '\n'.join(all_instructions)
    validation_errors = []
    name = request.form.get('recipe_name', '')
    description = request.form.get('recipe_description', '')
    time = request.form.get('recipe_time', '')
    ingredients = request.form.get('ingredients', '')
    instructions = request.form.get('instructions', '')

    # Validate the recipe name. It can not be empty or longer than 50 characters long.

    if len(name) == 0 or len(name) > 50:
        validation_errors.append('The title should not be empty or longer than 50 characters long.'
                                 )

    # Validate the recipe description. It can not be empty or longer than 185 characters long.

    if len(description) == 0 or len(description) > 500:
        validation_errors.append('The description should not be empty or longer than 500 characters long.'
                                 )

    # Validate the recipe time. It can not be empty or longer than 12 characters long (enough space for a 3 digit number and a unit of measurement).

    if len(time) == 0 or len(time) > 12:
        validation_errors.append('The recipe time should not be empty or longer than 12 characters long.'
                                 )

    # Validate the recipe ingredients. It can not be empty or longer than 1000 characters long.

    if len(ingredients) == 0 or len(ingredients) > 1000:
        validation_errors.append('The list of ingredients should not be empty or longer than 1000 characters long.'
                                 )

    # Validate the recipe instructions. It can not be empty or longer than 1500 characters long.

    if len(instructions) == 0 or len(instructions) > 1500:
        validation_errors.append('The list of instructions should not be empty or longer than 1500 characters long.'
                                 )

    # If no errors on validation, display error message.

    if len(validation_errors) > 0:
        error_string = '\n'.join(validation_errors)
        return render_template(
            'editrecipe.html',
            page_title='Edit Recipe',
            errors=error_string,
            recipe=the_recipe,
            cuisines=all_cuisines,
            ingredients=each_ingredient,
            instructions=each_instruction,
            )

    recipes.update({'_id': ObjectId(recipe_id)}, {
        'recipe_name': input_data['recipe_name'],
        'recipe_description': input_data['recipe_description'],
        'recipe_cost': input_data['recipe_cost'],
        'recipe_time': input_data['recipe_time'],
        'is_healthy': request.form.get('is_healthy'),
        'is_vegetarian': request.form.get('is_vegetarian'),
        'recipe_cuisine_image': input_data['recipe_cuisine_image'],
        'ingredients': all_ingredients,
        'instructions': all_instructions,
        })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """ Deletes the selected recipe. Uses a Javascript function to confirm delete in <script> tags at the bottom of the template
    """

    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=True)
