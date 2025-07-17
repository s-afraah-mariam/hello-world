from flask import Flask, render_template
from model import db, Task

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/')
    def home():
        tasks = Task.query.all()  # Read from database
        return render_template('home.html', tasks=tasks)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()

        # Insert sample data only once
        if not Task.query.first():
            db.session.add_all([
                Task(title="Learn Flask"),
                Task(title="Connect to SQLite"),
                Task(title="Render with Jinja2")
            ])
            db.session.commit()

    app.run(debug=True)
