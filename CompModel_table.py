from Company_EtoE_flask_UI_CRUD.Compappconfig import *

class COMPANY(db.Model):
    __tablename__='company_info'
    compId=db.Column('company_id',db.Integer,primary_key=True)
    compName=db.Column('company_name',db.String(100))
    compProf=db.Column('company_profit',db.Float())

    def __str__(self):
        return f'''
                Company ID:{self.compId}
                Company Name:{self.compName}
                Company Profit:{self.compProf}'''
    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    #db.create_all()
    #print('Table reated.....')
    pass
