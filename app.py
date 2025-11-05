from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fragrances.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)  # Needed for form submissions and Flask security

db = SQLAlchemy(app)

# Fragrance model
class Fragrance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(200))
    price = db.Column(db.String(50))
    bottle_size = db.Column(db.String(50))
    image = db.Column(db.String(200), default="placeholder.jpg")

    def __repr__(self):
        return f'<Fragrance {self.name}>'

# Homepage - display all fragrances
@app.route('/')
def home():
    search_query = request.args.get('search')
    if search_query:
        fragrances = Fragrance.query.filter(Fragrance.name.ilike(f"%{search_query}%")).all()
    else:
        fragrances = Fragrance.query.all()
    return render_template('index.html', fragrances=fragrances)

# Add a new fragrance
@app.route('/add', methods=['GET', 'POST'])
def add_fragrance():
    if request.method == 'POST':
        name = request.form['name']
        notes = request.form['notes']
        price = request.form['price']
        bottle_size = request.form['bottle_size']
        image = request.form['image'] or "placeholder.jpg"

        new_fragrance = Fragrance(name=name, notes=notes, price=price, bottle_size=bottle_size, image=image)
        db.session.add(new_fragrance)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

# Edit a fragrance
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_fragrance(id):
    fragrance = Fragrance.query.get_or_404(id)
    if request.method == 'POST':
        fragrance.name = request.form['name']
        fragrance.notes = request.form['notes']
        fragrance.price = request.form['price']
        fragrance.bottle_size = request.form['bottle_size']
        fragrance.image = request.form['image'] or "placeholder.jpg"
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', fragrance=fragrance)

# Delete a fragrance
@app.route('/delete/<int:id>', methods=['POST'])
def delete_fra_
