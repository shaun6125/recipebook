from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(45), unique=True, nullable=False)
    recipies = db.relationship("Recipe", backref="category", cascade="all, delete", lazy=True)
    users = db.relationship("User", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Recipe(db.Model):
    # schema for the recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_country = db.Column(db.String(50), unique=True, nullable=False)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_serves = db.Column(db.String(50), unique=True, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Country: {1} | Name: {2}".format(
            self.id, self.recipe_country, self.recipe_name
        )


class User(db.Model):
    # schema for the user model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    user_email = db.Column(db.String(50), unique=True, nullable=False)
    user_password = db.Column(db.String(50), unique=True, nullable=False)   
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Name: {1} | Email: {2}".format(
            self.id, self.user_name, self.user_email
        )