from flask import Blueprint

users = Blueprint('users', __name__)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user1 = User(username=form.username.data, email=form.email.data, password=pw)
        db.session.add(user1)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user1 = User.query.filter_by(email=form.email.data).first()
        if user1 and bcrypt.check_password_hash(user1.password, form.password.data):
            login_user(user1, remember=form.remember.data)
            if len(url_stack):
                url = url_stack.pop()
                url_stack.clear()
                return redirect(url)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please try again.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
    

@app.route("/account")
def account():
    if current_user.is_authenticated:
        posts=Post.query.filter_by(author=current_user).all()
        imagefile = url_for('static', filename='Images/' + current_user.image_file)
        return render_template('account.html', posts=posts, title='Account', image_file=imagefile)
    else:
        url_stack.append(url_for('account'))
        flash(f'You are not logged in.', 'danger')
        return redirect(url_for('login'))