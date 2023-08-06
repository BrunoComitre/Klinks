from flask import (jsonify, request, render_template)
from config import create_app
from models import db, City
from forms import CityForm


app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = CityForm()
        return render_template('index.html', form=form)
    
    if request.method == 'POST':
        bound_form = CityForm(data=request.get_json())

        if bound_form.validate_on_submit():
            city_name = bound_form.name.data
            city_obj = City(name=city_name)
            db.session.add(city_obj)
            db.session.commit()
            return jsonify (city_obj)
        
        return jsonify({'errors': bound_form.errors})


if __name__ == '__main__':
    app.run()
