from flask import Flask,render_template,request

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

ai=Flask(__name__)
ai.config['SECRET_KEY']='csrftoken'

class Nameform(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField()


@ai.route('/webforms',methods=['GET','POST'])

def webforms():
    form=Nameform()
    if request.method=='POST':
        form=Nameform(request.form)
        if form.validate():
            print(form.name.data)
            return 'Success'

    return render_template('webforms.html',form=form)


if __name__=='__main__':
    ai.run(debug=True)