from flask import Flask, request, jsonify
import requests
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_recipes(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={app.config['SPOONACULAR_API_KEY']}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/')
def home():
    return "Welcome to the Recipe Recommendation System"

@app.route('/recipes', methods=['GET'])
def recipes():
    ingredients = request.args.get('ingredients')
    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400
    recipes = get_recipes(ingredients)
    if "error" in recipes:
        return jsonify({"error": recipes["error"]}), 500
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)
