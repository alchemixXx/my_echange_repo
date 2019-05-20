from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskblog import db, bcrypt, mail
from flaskblog.team.forms import TeamForm, UpdateTeamForm
from flaskblog.models import Team
from flask_login import login_required
from flaskblog.utils import save_picture


team = Blueprint('team', __name__)

@team.route("/team/new", methods=['GET', 'POST'])
@login_required
def new_teammate():
    form = TeamForm()
    if form.validate_on_submit():
        if form.education.data != "":
            education = form.education.data
        else:
            education = "None"
        # if form.employer.data != "":
        #     employer = form.employer.data
        # else:
        #     employer = "None"
        if form.position.data != "":
            position = form.position.data
        else:
            position = "None"
        if form.work.data != "":
            work = form.work.data
        else:
            work = "None"
        if form.work_position.data != "":
            work_position = form.work_position.data
        else:
            work_position = "None"
        if form.social_link.data != "":
            social_link = form.social_link.data
        else:
            social_link = "None"
        if form.biography.data != "":
            biography = form.biography.data
        else:
            biography = "None"
        picture = save_picture(form.picture.data)
        image_file = url_for('static', filename='teammate_pics/' + picture)
        teammate = Team(name=form.name.data, education=education, work=work,
                         work_position=work_position,
                         position=position, social_link=social_link,
                         image_file=image_file, biography=biography)
        db.session.add(teammate)
        db.session.commit()
        flash('Teammate created', 'success')
        return redirect(url_for('main.team'))
    return render_template('00_create_teammate.html', title="New Teammate", form=form)


@team.route("/team/<int:teammate_id>")
def teammate(teammate_id):
    teammate = Team.query.get_or_404(teammate_id)
    return render_template('13_specific_teammate.html', title=teammate.name, post=teammate,  image_file=teammate.image_file)


@team.route("/team/<int:teammate_id>/update", methods=['GET', 'POST'])
@login_required
def update_teammate(teammate_id):
    teammate = Team.query.get_or_404(teammate_id)
    # if post.author != current_user
    # if current_user:
    #     abort(403)
    form = UpdateTeamForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            teammate.image_file = url_for('static', filename='teammate_pics/' + picture_file)
        teammate.name = form.name.data
        teammate.education = form.education.data
        teammate.work = form.work.data
        teammate.work_position = form.work_position.data
        # teammate.employer = form.employer.data
        teammate.position = form.position.data
        teammate.social_link = form.social_link.data
        teammate.biography = form.biography.data
        # picture = form.file_name.data
        # image_file = url_for('static', filename='doctor_pics/' + picture)

        db.session.commit()
        flash('Teammate has been updated', 'success')
        return redirect(url_for('team.teammate', teammate_id=teammate.id))
    elif request.method == "GET":
        form.name.data = teammate.name
        form.education.data = teammate.education
        form.work.data = teammate.work
        form.work_position.data = teammate.work_position
        # form.employer.data = teammate.employer
        form.position.data = teammate.position
        form.social_link.data = teammate.social_link
        form.biography.data = teammate.biography
        form.picture.data = teammate.image_file
    # return render_template('00_create_post.html', title="Update Post",
    #                        form=form, legend="Update Post")
    image_file = url_for('static', filename='teammate_pics/' + teammate.image_file)
    return render_template('00_create_teammate.html', title="Update Teammate",
                           form=form, image_file=image_file)


@team.route("/team/<int:teammate_id>/delete", methods=['POST'])
@login_required
def delete_teammate(teammate_id):
    teammate = Team.query.get_or_404(teammate_id)

    # if post.author != current_user
    # if current_user:
    #     abort(403)
    db.session.delete(teammate)
    db.session.commit()
    flash('Teammate has been deleted!', 'success')
    return redirect(url_for('main.team'))