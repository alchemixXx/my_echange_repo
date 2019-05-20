from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskblog import db, bcrypt, mail
from flaskblog.organizations.forms import OrganizationForm, UpdateOrganiztionForm
from flaskblog.models import Partners
from flask_login import login_required


organizations = Blueprint('organizations', __name__)

# About - first navbar section


@organizations.route("/organization/new", methods=['GET', 'POST'])
@login_required
def new_organization():
    form = OrganizationForm()
    if form.validate_on_submit():
        if form.link.data != "":
            link = form.link.data
        else:
            link = "None"
        if form.specialization.data != "":
            specialization = form.specialization.data
        else:
            specialization = "None"
        if form.city.data != "":
            city = form.city.data
        else:
            city = "None"
        if form.country.data != "":
            country = form.country.data
        else:
            country = "None"
        if form.content.data != "":
            content = form.content.data
        else:
            content = "None"
        picture = form.file_name.data
        image_file = url_for('static', filename='partners_pics/' + picture)
        org = Partners(title=form.title.data, address=form.address.data, link=link, specialization=specialization,
                         image_file=image_file, city=city, country=country, content=content)
        db.session.add(org)
        db.session.commit()
        flash('Organization created', 'success')
        return redirect(url_for('main.organizations'))
    return render_template('00_create_organization.html', title="New Organization", form=form)


@organizations.route("/organizations/<int:orgs_id>")
def orgs(orgs_id):
    orgs = Partners.query.get_or_404(orgs_id)
    return render_template('41_specific_organization.html', title=orgs.title, post=orgs,  image_file=orgs.image_file)

@organizations.route("/organizations/<int:orgs_id>/update", methods=['GET', 'POST'])
@login_required
def update_org(orgs_id):
    org = Partners.query.get_or_404(orgs_id)
    # if post.author != current_user
    # if current_user:
    #     abort(403)
    form = UpdateOrganiztionForm()
    if form.validate_on_submit():
        org.title = form.title.data
        org.address = form.address.data
        org.content = form.content.data
        org.specialization = form.specialization.data
        org.link = form.link.data
        org.city = form.city.data
        org.country = form.country.data

        picture = form.file_name.data
        image_file = url_for('static', filename='orgs_pics/' + picture)

        db.session.commit()
        flash('Organization has been updated', 'success')
        return redirect(url_for('organizations.orgs', orgs_id=org.id))
    elif request.method == "GET":

        form.title.data = org.title
        form.address.data = org.address
        form.specialization.data = org.specialization
        form.content.data = org.content
        form.link.data = org.link
        form.city.data = org.city
        form.country.data = org.country
        form.picture.data = org.image_file
    # return render_template('00_create_post.html', title="Update Post",
    #                        form=form, legend="Update Post")
    return render_template('00_create_organization.html', title="Update Organization",
                           form=form)


@organizations.route("/organizations/<int:orgs_id>/delete", methods=['POST'])
@login_required
def delete_org(orgs_id):
    org = Partners.query.get_or_404(orgs_id)

    # if post.author != current_user
    # if current_user:
    #     abort(403)
    db.session.delete(org)
    db.session.commit()
    flash('Organization has been deleted!', 'success')
    return redirect(url_for('main.organizations'))