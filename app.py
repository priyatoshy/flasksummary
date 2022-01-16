#importing flask
from flask import Flask,request,redirect,render_template
from summary import TEXTE
 
#initializing the flask applications

app=Flask(__name__)


#CREATING END POINT RPOUTES

@app.route("/",methods=['GET','POST'])
def summary():
    if request.method=='POST':
        text_label=request.form['text_label']
        text_data=request.form['text_data']
        text_summarizer=TEXTE(text_data)
        text_summary=text_summarizer.summary()

      

        return render_template('result.html',text_data=text_data,text_summary=text_summary)

    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
