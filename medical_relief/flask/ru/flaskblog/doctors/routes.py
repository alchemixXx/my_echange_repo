from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskblog import db, bcrypt, mail
from flaskblog.doctors.forms import DoctorForm, UpdateDoctorForm
from flaskblog.models import Doctors
from flask_login import login_required
from flaskblog.utils import save_picture


doctors = Blueprint('doctors', __name__)

# About - first navbar section


@doctors.route("/doctors/new", methods=['GET', 'POST'])
@login_required
def new_doctor():
    form = DoctorForm()
    if form.validate_on_submit():
        if form.academic_degree.data != "":
            academic_degree = form.academic_degree.data
        else:
            academic_degree = "None"
        if form.employer.data != "":
            employer = form.employer.data
        else:
            employer = "None"
        if form.position.data != "":
            position = form.position.data
        else:
            position = "None"
        if form.city.data != "":
            city = form.city.data
        else:
            city = "None"
        if form.age.data != "":
            age = form.age.data
        else:
            age = "None"
        if form.biography.data != "":
            biography = form.biography.data
        else:
            biography = "None"
        picture = save_picture(form.picture.data)
        image_file = url_for('static', filename='doctor_pics/' + picture)
        doctor = Doctors(name=form.name.data, sex=form.sex.data, specialization=form.specialization.data,
                         academic_degree=academic_degree, employer=employer,
                         position=position, city=city, age=age,
                         image_file=image_file, biography=biography)
        db.session.add(doctor)
        db.session.commit()
        flash('Doctor created', 'success')
        return redirect(url_for('main.doctors'))
    return render_template('00_create_doctor.html', title="New Doctor", form=form)


@doctors.route("/doctors/<int:doctor_id>")
def doctor(doctor_id):
    doctor = Doctors.query.get_or_404(doctor_id)
    return render_template('42_specific_doctor.html', title=doctor.name, post=doctor,  image_file=doctor.image_file)


@doctors.route("/doctors/<int:doctor_id>/update", methods=['GET', 'POST'])
@login_required
def update_doc(doctor_id):
    doctor = Doctors.query.get_or_404(doctor_id)
    # if post.author != current_user
    # if current_user:
    #     abort(403)
    form = UpdateDoctorForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            doctor.image_file = url_for('static', filename='doctor_pics/' + picture_file)
        doctor.name = form.name.data
        doctor.sex = form.sex.data
        doctor.specialization = form.specialization.data
        doctor.academic_degree = form.academic_degree.data
        doctor.employer = form.employer.data
        doctor.position = form.position.data
        doctor.city = form.city.data
        doctor.age = form.age.data
        doctor.biography = form.biography.data
        # picture = form.file_name.data
        # image_file = url_for('static', filename='doctor_pics/' + picture)

        db.session.commit()
        flash('Doctor has been updated', 'success')
        return redirect(url_for('doctors.doctor', doctor_id=doctor.id))
    elif request.method == "GET":
        form.name.data = doctor.name
        form.sex.data = doctor.sex
        form.specialization.data = doctor.specialization
        form.academic_degree.data = doctor.academic_degree
        form.employer.data = doctor.employer
        form.position.data = doctor.position
        form.city.data = doctor.city
        form.age.data = doctor.age
        form.biography.data = doctor.biography
        form.picture.data = doctor.image_file
    # return render_template('00_create_post.html', title="Update Post",
    #                        form=form, legend="Update Post")
    image_file = url_for('static', filename='doctor_pics/' + doctor.image_file)
    return render_template('00_create_doctor.html', title="Update Doctor",
                           form=form, image_file=image_file)


@doctors.route("/doctors/<int:doctor_id>/delete", methods=['POST'])
@login_required
def delete_doctor(doctor_id):
    doctor = Doctors.query.get_or_404(doctor_id)

    # if post.author != current_user
    # if current_user:
    #     abort(403)
    db.session.delete(doctor)
    db.session.commit()
    flash('Doctor has been deleted!', 'success')
    return redirect(url_for('main.doctors'))