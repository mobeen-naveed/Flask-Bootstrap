from flask import Flask, render_template, url_for, redirect, flash, request, jsonify, make_response
from forms import ContactForm
import gold_scrape as gs

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245' ## Add secret key for preventing Cross Site Scripting

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title="Home")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    # GET request, show page only 
    if request.method == "GET":
        form = ContactForm()
        # return render_template('contact.html', title="Contact Us", form=form)   
        return render_template('contact.html', title="Contact Us", form=form)    
    
    # POST request, return json response accordingly
    else:
        
        contact_name = None
        contact_email = None
        contact_message = None

        try:
            contact_name =  request.form['contact_name']
            contact_email = request.form['contact_email']
            contact_message = request.form['contact_message']

            print(f'contact_name == {contact_name}, contact_email == {contact_email}, contact_message == {contact_message}')

            return make_response(jsonify({'message': '<b>Thank You!</b> We will get back to you as soon as we can'}), 200)

        except Exception as ex:
            print(f'contact_name == {contact_name}, contact_email == {contact_email}, contact_message == {contact_message}, exception == {str(ex)}')
            return make_response(jsonify({'message':'<b>Sorry!</b> We faced some issue while submiting your details'}), 500)    

@app.route('/get_goldrates', methods=['GET'])
def getGoldRatesForFooter():
    return make_response(jsonify({'footer_data': gs.getGoldRates()}), 200)

if __name__ == '__main__':
    app.run(debug=True)    