from flask import Flask,request,render_template
from orm.bank_prob_stmt.serviceimpl import BankServiceImpl
from orm.bank_prob_stmt.daoimpl import BankCrudOp
from orm.bank_prob_stmt.models import app,Account,db

accountTypes = {"S":"Saving","C":"Current"}

service = BankServiceImpl()

def dummyAccount():
    return Account(id=0,type='',balance=0.0)

@app.route("/account/welcome/")
def welcome_account():
    return render_template('account.html',acc=dummyAccount(),
                           accTypes = accountTypes,
                           accounts = service.get_all_active_bank_accounts())
@app.route("/account/save/",methods=["post"])
def save_account():
    accob = Account(type=request.form["type"],balance=request.form["balance"])
    db.session.add(accob)
    db.session.commit()
    return render_template('account.html', acc=dummyAccount(),
                           accTypes=accountTypes,
                           accounts=service.get_all_active_bank_accounts())

if __name__ == '__main__':
    app.run(debug=True)
