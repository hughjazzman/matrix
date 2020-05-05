"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from matrix import app
from .ops import *

test = Matrix(2,2,5)
test2 = Matrix()
test3 = Matrix()

#@app.route('/')
@app.route('/', methods = ['GET', 'POST'])
def home():
    """Renders the home page."""
    if request.method == 'POST':
        if 'submit_swap' in request.form:
            row1 = request.form['row1_swap']
            row2 = request.form['row2_swap']
            try:
                row1, row2 = int(row1)-1, int(row2)-1
            except ValueError:
                return render_template('WebPage1.html', matrix = test, error = 1)
            except:
                pass
            if not test.valid_row(row1) or not test.valid_row(row2):
                return render_template('WebPage1.html', matrix = test, error = 1)
            test.swap_row(row1,row2)
        elif 'submit_mul' in request.form:
            row = request.form['row_mul']
            scalar = request.form['scalar_mul']
            try:
                row, scalar = int(row)-1, test.frac_to_float(scalar)
            except ValueError:
                return render_template('WebPage1.html', matrix = test, error = 1)
            except:
                pass
            if not test.valid_row(row) or scalar == 0:
                return render_template('WebPage1.html', matrix = test, error = 1)
            test.scalar_row(row,scalar)
        elif 'submit_add' in request.form:
            scalar = request.form['scalar_add']
            row_from = request.form['row_from']
            row_to = request.form['row_to']
            try:
                row_from, row_to, scalar = int(row_from)-1,int(row_to)-1, test.frac_to_float(scalar)
            except ValueError:
                return render_template('WebPage1.html', matrix = test, error = 1)
            except:
                pass
            if not test.valid_row(row_from) or not test.valid_row(row_to):
                return render_template('WebPage1.html', matrix = test, error = 1)
            test.scalar_add(row_to,row_from,scalar)
        
        return render_template('WebPage1.html', matrix=test, error = 0)
        
    elif request.method == 'GET':
        return render_template('WebPage1.html', matrix = test, error = 0)


#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
