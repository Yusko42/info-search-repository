from flask import (
    Flask, render_template, redirect,
    url_for, flash, request
)

from flask_login import (
    LoginManager, login_user,
    logout_user, login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models import db, User, University, Student
from forms import (
    UniversityForm,
    StudentForm,
    RegistrationForm,
    LoginForm
)


app = Flask(__name__)

app.config['SECRET_KEY'] = 'replace-with-a-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'
login_manager.login_message = 'Для выполнения этого действия необходимо войти в систему.'

from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(
            username=form.username.data
        ).first()

        if existing_user:
            flash('Такой пользователь уже существует')
        else:
            user = User(
                username=form.username.data,
                password=generate_password_hash(
                    form.password.data
                )
            )

            db.session.add(user)
            db.session.commit()

            flash('Регистрация прошла успешно')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data
        ).first()

        if user and check_password_hash(
            user.password,
            form.password.data
        ):
            login_user(user)
            return redirect(url_for('university_list'))

        flash('Неверный логин или пароль')

    return render_template('login.html', form=form)


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('university_list'))

# CRUD

@app.route('/universities')
def university_list():
    universities = University.query.all()

    return render_template(
        'university/university_list.html',
        universities=universities
    )

@app.route('/universities/create', methods=['GET', 'POST'])
@login_required
def university_create():
    form = UniversityForm()

    if form.validate_on_submit():
        university = University(
            full_name=form.full_name.data,
            short_name=form.short_name.data,
            founded_date=form.founded_date.data
        )

        db.session.add(university)
        db.session.commit()

        return redirect(url_for('university_list'))

    return render_template(
        'university/university_form.html',
        form=form
    )

@app.route('/universities/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def university_update(id):
    university = db.get_or_404(University, id)
    form = UniversityForm(obj=university)

    if form.validate_on_submit():
        form.populate_obj(university)
        db.session.commit()

        return redirect(url_for('university_list'))

    return render_template(
        'university/university_form.html',
        form=form
    )

@app.route('/universities/<int:id>/delete', methods=['GET', 'POST'])
def university_delete(id):
    university = db.get_or_404(University, id)

    if request.method == 'POST':
        if university.students:
            flash('Нельзя удалить университет, в котором есть студенты')
        else:
            db.session.delete(university)
            db.session.commit()

        return redirect(url_for('university_list'))

    return render_template(
        'confirm_delete.html',
        object=university
    )

# Student CRUD

@app.route('/students')
def student_list():
    students = Student.query.all()

    return render_template(
        'student/student_list.html',
        students=students
    )

@app.route('/students/create', methods=['GET', 'POST'])
@login_required
def student_create():
    form = StudentForm()

    form.university_id.choices = [
        (u.id, u.short_name)
        for u in University.query.all()
    ]

    if form.validate_on_submit():
        student = Student(
            full_name=form.full_name.data,
            birth_date=form.birth_date.data,
            university_id=form.university_id.data,
            enrollment_year=form.enrollment_year.data
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('student_list'))

    return render_template(
        'student/student_form.html',
        form=form
    )

@app.route('/students/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def student_update(id):
    student = db.get_or_404(Student, id)
    form = StudentForm(obj=student)

    form.university_id.choices = [
        (u.id, u.short_name)
        for u in University.query.all()
    ]

    if form.validate_on_submit():
        student.full_name = form.full_name.data
        student.birth_date = form.birth_date.data
        student.university_id = form.university_id.data
        student.enrollment_year = form.enrollment_year.data

        db.session.commit()

        return redirect(url_for('student_list'))

    return render_template(
        'student/student_form.html',
        form=form
    )

@app.route('/students/<int:id>/delete', methods=['GET', 'POST'])
def student_delete(id):
    student = db.get_or_404(Student, id)

    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()

        return redirect(url_for('student_list'))

    return render_template(
        'confirm_delete.html',
        object=student
    )

if __name__ == '__main__':
    app.run(debug=True)