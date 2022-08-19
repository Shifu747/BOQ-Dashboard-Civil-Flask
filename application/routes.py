from audioop import add
from application import app, db
from flask import render_template, flash, redirect, url_for, get_flashed_messages
from application.form import UserInputForm
from application.models import Boq
import json
import sqlite3
import pandas as pd


@app.route('/index')
def index():
    entries = Boq.query.order_by(Boq.date.desc()).all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['GET','POST'])
def add():
    form = UserInputForm()
    if form.validate_on_submit():
        entry = Boq(item=form.item.data, quantity=form.quantity.data, unit=form.unit.data,
                    rate= form.rate.data, total=form.quantity.data*form.rate.data )
        db.session.add(entry)
        db.session.commit()
        flash('Successfull entry', 'success')
        return redirect(url_for('index'))
    return render_template('add.html', title='Add', form=form)

@app.route('/delete/<int:entry_id>')
def delete(entry_id):
    entry = Boq.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash('Deletion was success', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    dates = db.session.query(db.func.sum(Boq.total), Boq.date).group_by(Boq.date).order_by(Boq.date).all()

    total_bill = []
    date_labels = []
    for total, date in dates:
        if (len(total_bill)!=0):
            total_bill.append(total_bill[-1] + total)
        else:
            total_bill.append(total)
        date_labels.append(date.strftime('%d-%m-%Y'))

    items = db.session.query(db.func.sum(Boq.total), Boq.item).group_by(Boq.item).order_by(Boq.item).all()

    item_labels = []
    item_bill = []
    for bill, name in items:
        if name not in item_labels:
            item_labels.append(name)
        else:
            continue
        item_bill.append(bill)
    
    return render_template('dashboard.html',
            total_bill = json.dumps(total_bill),
            date_labels = json.dumps(date_labels),
            item_bill = json.dumps(item_bill),
            item_labels = json.dumps(item_labels)

    )

@app.route('/tocsv')
def tocsv():
    path = "D:\\Flask\\BOQ-Dashboard\\application"
    database = path + "\\boqDB.db"
    cnx = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * FROM boq", cnx)
    df.to_csv("D:\\Flask\\BOQ-Dashboard\\application\\boq.csv", index=False)
    flash('Exporting was successful', 'success')
    return redirect(url_for('index'))
