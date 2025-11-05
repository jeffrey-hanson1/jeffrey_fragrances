from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fragrances.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
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

# Homepage route with search
@app.route('/')
def home():
    search_query = request.args.get('q')
    if search_query:
        fragrances = Fragrance.query.filter(Fragrance.name.ilike(f"%{search_query}%")).all()
    else:
        fragrances = Fragrance.query.all()
    return render_template('index.html', fragrances=fragrances, search_query=search_query)

# Add new fragrance route
@app.route('/add', methods=['GET', 'POST'])
def add_fragrance():
    if request.method == 'POST':
        name = request.form.get('name')
        notes = request.form.get('notes')
        price = request.form.get('price')
        bottle_size = request.form.get('bottle_size')
        image = request.form.get('image') or 'placeholder.jpg'

        new_fragrance = Fragrance(
            name=name,
            notes=notes,
            price=price,
            bottle_size=bottle_size,
            image=image
        )
        db.session.add(new_fragrance)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')

# Edit fragrance route
@app.route('/edit/<int:fragrance_id>', methods=['GET', 'POST'])
def edit_fragrance(fragrance_id):
    fragrance = Fragrance.query.get_or_404(fragrance_id)

    if request.method == 'POST':
        fragrance.name = request.form.get('name')
        fragrance.notes = request.form.get('notes')
        fragrance.price = request.form.get('price')
        fragrance.bottle_size = request.form.get('bottle_size')
        fragrance.image = request.form.get('image') or 'placeholder.jpg'

        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', fragrance=fragrance)

# Delete fragrance route
@app.route('/delete/<int:fragrance_id>', methods=['POST'])
def delete_fragrance(fragrance_id):
    fragrance = Fragrance.query.get_or_404(fragrance_id)
    db.session.delete(fragrance)
    db.session.commit()
    return redirect(url_for('home'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
