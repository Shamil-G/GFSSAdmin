from flask import render_template, flash, request,  Response, redirect, g, make_response
from flask_login import login_required, current_user, logout_user
from datetime import date
from model.utils import *
# from model.testing import *
from model.model_login import *
from main_app import app, log
import app_config as cfg


if cfg.debug_level > 0:
    print("Routes стартовал...")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/programs', methods=['GET', 'POST'])
@login_required
def view_programs():
    return render_template("programs.html", cursor=programs())


@app.route('/program-del/<int:id_task>')
@login_required
def view_program_del(id_task):
    program_delete(id_task)
    return render_template("programs.html", cursor=programs())

@app.route('/')
@app.route('/roles')
@login_required
def view_roles():
    return render_template("roles.html", cursor=all_roles())


@app.route('/alter-role/<int:id_user>/<string:role_name>')
@login_required
def view_alter_role_users(id_user, role_name):
    alter_role(id_user, role_name)
    return redirect(url_for('view_list_users'))


@app.route('/role-delete/<int:id_role>')
@login_required
def view_role_delete(id_role):
    role_delete(id_role)
    return render_template("roles.html", cursor=all_roles())


@app.route('/role-add', methods=['POST', 'GET'])
@login_required
def view_role_add():
    if cfg.debug_level > 1:
        print("Добавляем  Роль !")
    if request.method == "POST":
        try:
            name = request.form['name_role']
            full_name = request.form['full_name_role']
            role_add(name, full_name)
        finally:
            if cfg.debug_level > 0:
                print("ROLE_ADD. Вход по GET")
            return redirect("/roles")
    return render_template("role-add.html")


@app.route('/role-detail/<int:id_role>', methods=['POST', 'GET'])
@login_required
def view_role_upd(id_role):
    if cfg.debug_level > 1:
        print("Обновляем роль!")
    if request.method == "POST":
        try:
            name = request.form['name_role']
            full_name = request.form['full_name_role']
            role_upd(id_role, name, full_name)
        finally:
            if cfg.debug_level > 0:
                print("ROLE_UPD. Вход по GET")
            return redirect("/roles")
    return render_template("role-upd.html")


@app.route('/role-detail/<int:id_role>')
@login_required
def view_role_detail(id_role):
    return render_template("roles.html", cursor=all_roles())


@app.route('/role-users/<int:id_role>')
@login_required
def view_role_users(id_role):
    _all_users = all_users()
    _role_users = role_users(id_role)
    role_name = get_role_name(id_role)
    for user in _role_users:
        _all_users.remove(user)
    return render_template("role-users.html", id_role=id_role, role_name=role_name,
                           all_users=_all_users, role_users=_role_users)


@app.route('/role-users-add/<int:id_role>/<int:id_user>')
@login_required
def view_role_users_add(id_role, id_user):
    role_user_add(id_role, id_user)
    return redirect(url_for('view_role_users', id_role=id_role))


@app.route('/role-users-del/<int:id_role>/<int:id_user>')
@login_required
def view_role_users_del(id_role, id_user):
    role_user_del(id_role, id_user)
    return redirect(url_for('view_role_users', id_role=id_role))


@app.route('/list-users')
@login_required
def view_list_users():
    return render_template("list_users.html", cursor=list_users())


@app.route('/load-users')
@login_required
def view_load_users():
    load_operators('operators.xlsx')
    return redirect(url_for('view_list_users', cursor=list_users()))


@app.route('/user/<int:id_user>', methods=['POST', 'GET'])
@login_required
def user_page(id_user):
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        iin = request.form['iin']
        phone = ''
        if 'phone' in request.form:
            phone = request.form['phone']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        description = request.form['description']
        if type(password) is str and password != '':
            hash_pwd = generate_password_hash(password)
        else:
            hash_pwd = ''
        log.info(f'USER PAGE. POST. ID_USER: {id_user}, IIN: {iin}, username: {username}, password: {password}')
        set_user_info(id_user, username, hash_pwd, iin, phone, last_name, first_name, middle_name, description)
        return redirect(url_for('view_list_users'))
    log.info(f'USER PAGE. GET ID_USER: {id_user}')
    username, iin, phone, last_name, first_name, middle_name, description = get_user_info(id_user)
    password = ''
    return render_template("user.html", username=username, password=password, iin=iin, phone=phone, last_name=last_name,
                           first_name=first_name, middle_name=middle_name, description=description)


