from flask import render_template, url_for
from app import app

@app.route('/', methods = ['GET', 'POST'])
@app.route('/title', methods = ['GET', 'POST'])
def title():
    return render_template(
        'title.html'
    )

@app.route('/1')
def profile_1():
    return render_template(
        '1.html'
    )

@app.route('/2')
def profile_2():
    return render_template(
        '2.html'
    )

@app.route('/3')
def profile_3():
    return render_template(
        '3.html'
    )

@app.route('/4')
def profile_4():
    return render_template(
        '4.html'
    )

@app.route('/5')
def profile_5():
    return render_template(
        '5.html'
    )

@app.route('/6')
def profile_6():
    return render_template(
        '6.html'
    )

@app.route('/7')
def profile_7():
    return render_template(
        '7.html'
    )

@app.route('/8')
def profile_8():
    return render_template(
        '8.html'
    )

@app.route('/9')
def profile_9():
    return render_template(
        '9.html'
    )

@app.route('/10')
def profile_10():
    return render_template(
        '10.html'
    )

@app.route('/11')
def profile_11():
    return render_template(
        '11.html'
    )

@app.route('/12')
def profile_12():
    return render_template(
        '12.html'
    )

@app.route('/13')
def profile_13():
    return render_template(
        '13.html'
    )

@app.route('/14')
def profile_14():
    return render_template(
        '14.html'
    )

@app.route('/15')
def profile_15():
    return render_template(
        '15.html'
    )

@app.route('/16')
def profile_16():
    return render_template(
        '16.html'
    )
