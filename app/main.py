from flask import (jsonify, request, render_template)
from config import create_app
from models import db, Links
from forms import LinkForm


app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = LinkForm()
        return render_template('index.html', form=form)
    
    if request.method == 'POST':
        bound_form = LinkForm(data=request.get_json())

        if bound_form.validate_on_submit():
            link_name = bound_form.name.data
            link_obj = Links(name=link_name)
            db.session.add(link_obj)
            db.session.commit()
            return jsonify (link_obj)
        
        return jsonify({'errors': bound_form.errors})


if __name__ == '__main__':
    app.run()
