from flask import Flask, render_template, render_template_string, jsonify

app = Flask(__name__)


recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}


@app.route("/")
def homepage():
    return render_template_string(
        """
            <h1>Homepage</h1>
        """
    )


@app.route("/recipes/<rec_id>")
def show_recipt(rec_id):
    try:
        recipe_id = int(rec_id)
        if recipe_id in recipes:
            return jsonify(recipes[recipe_id])
        else:
            return jsonify({"error": "Recipe not found"}), 404
    except ValueError:
        return jsonify({"error": "Invalid recipe ID (must be integer)"}), 400


if __name__ == "__main__":
    app.run(debug=True)