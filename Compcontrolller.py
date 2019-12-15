from Company_EtoE_flask_UI_CRUD.Compappconfig import *
from Company_EtoE_flask_UI_CRUD.CompModel_table import *
from flask import Flask,render_template,request,redirect,url_for



@app.route('/')
def loading_comp_detail():
    msg=''
    return render_template('Comphome.html',ccmp=get_list_of_company(),dc=dummy_company(),MSG=msg)

def dummy_company():
    return COMPANY(compId=0,compName='',compProf=0.0)

def get_list_of_company():
    cmp = COMPANY.query.all()
    return cmp

@app.route('/save',methods=['POST'])
def save_company_detail():

    cidd=request.form['compId']
    c=COMPANY(compId=request.form['compId'],
              compName=request.form['compName'],compProf=request.form['compProf'])
    #if (c.compId)==0 or (c.compId)=='':
    if int(cidd) == 0:
        del c.compId
        db.session.add(c)
        db.session.commit()
        msg = "CompanyData save Successfully....."
        #return render_template('Comphome.html', MSG=msg, ccmp=get_list_of_company(), dc=dummy_company())
    else:
        #c = COMPANY(compId=request.form['compId'], compName=request.form['compName'], compProf=request.form['compProf'])
        cmpdbb = COMPANY.query.filter_by(compId=cidd).first()
        cmpdbb.compName = c.compName
        cmpdbb.compProf = c.compProf
        #db.session.add(cmpdb)
        db.session.commit()
        msg = "Data updated successfully..."
    return render_template('Comphome.html', MSG=msg,ccmp=get_list_of_company(),dc=dummy_company())

@app.route('/cmp/edit/<int:compIdd>',methods=["GET"])
def edit_company_data(compIdd):
    #id = request.form['compId']
    #nm = request.form['compName']
    #pr = request.form['compProf']
    print(compIdd)

    #c = COMPANY(compId=request.form['compId'],
                #compName=request.form['compName'],
                #compProf=request.form['compProf'])
    cmpdb = COMPANY.query.filter_by(compId=compIdd).first()
    #print(cmpdb)

    return render_template('Comphome.html',ccmp=get_list_of_company(),dc=cmpdb)

@app.route('/cmp/delete/<int:compIdd>',methods=["GET"])
def delete_company_data(compIdd):
    print('insude delete link',compIdd)
    deldb=COMPANY.query.filter_by(compId=compIdd).first()
    db.session.delete(deldb)
    db.session.commit()
    #msg = "Data updated successfully..."
    #return render_template('Comphome.html', MSG=msg,ccmp=get_list_of_company())
    return redirect(url_for('loading_comp_detail'))