from flask import Flask,request,render_template
from orm.bank_prob_stmt.serviceimpl import BankServiceImpl
from orm.bank_prob_stmt.daoimpl import BankCrudOp
from orm.bank_prob_stmt.models import app,Account

service = BankServiceImpl()




@app.route("/bank/welcome/")
def bank_welcome_page():
    return render_template('bank.html',
                           accounts = service.get_all_active_bank_accounts(),
                           customers =service.get_all_active_customers())