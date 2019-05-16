from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskblog import db, bcrypt, mail
from flaskblog.treatments.forms import TreatmentForm, UpdateTreatmentForm
from flaskblog.models import User, News, Treatment
from flask_login import login_required


treatment = Blueprint('treatment', __name__)

# About - first navbar section


@treatment.route("/treatment/new", methods=['GET', 'POST'])
@login_required
def new_treatment():
    form = TreatmentForm()
    if form.validate_on_submit():
        picture = form.file_name.data
        image_file = url_for('static', filename='treatment_pics/' + picture)
        treat = Treatment(title=form.title.data, content=form.content.data,
                         image_file=image_file, direction=form.direction.data)
        db.session.add(treat)
        db.session.commit()
        flash('Treatment created', 'success')
        return redirect(url_for('main.treatments_all'))
    return render_template('00_create_treatment.html', title="New Treatment", form=form)


@treatment.route("/treatment/<int:treat_id>")
def treat(treat_id):
    treat = Treatment.query.get_or_404(treat_id)
    return render_template('treatment.html', title=treat.title, post=treat,  image_file=treat.image_file)

@treatment.route("/treatment/<int:treat_id>/update", methods=['GET', 'POST'])
@login_required
def update_treat(treat_id):
    treat = Treatment.query.get_or_404(treat_id)
    # if post.author != current_user
    # if current_user:
    #     abort(403)
    form = TreatmentForm()
    if form.validate_on_submit():
        treat.title = form.title.data
        treat.content = form.content.data
        treat.direction = form.direction.data
        picture = form.file_name.data
        image_file = url_for('static', filename='treatment_pics/' + picture)

        db.session.commit()
        flash('Treatment has beend updated', 'success')
        return redirect(url_for('treatment.treat', treat_id=treat.id))
    elif request.method == "GET":
        form.title.data = treat.title
        form.direction.data = treat.direction
        form.content.data = treat.content
        form.picture.data = treat.image_file
    # return render_template('00_create_post.html', title="Update Post",
    #                        form=form, legend="Update Post")
    return render_template('00_create_treatment.html', title="Update Treatment",
                           form=form)


@treatment.route("/treatment/<int:treat_id>/delete", methods=['POST'])
@login_required
def delete_treat(treat_id):
    treat = Treatment.query.get_or_404(treat_id)

    # if post.author != current_user
    # if current_user:
    #     abort(403)
    db.session.delete(treat)
    db.session.commit()
    flash('Treatment has been deleted!', 'success')
    return redirect(url_for('main.treatments_all'))
