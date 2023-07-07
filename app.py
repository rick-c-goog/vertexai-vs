#write python flask input form, with input textbox, checkbox to select options,  output texbox, submit button
from flask import Flask, render_template, request
import os
from backend.property_llm import predict_llm_property
app = Flask(__name__)

@app.route("/submit", methods=['POST']) 
def submit():
    # Get the input from the user
    input_text = request.form.get("input_text")
    
    option_text = request.form.get("options")
    
    output_text=predict_llm_property(input_text, option_text)
    app.logger.info('output: %s ', output_text)
    return render_template("index.html", input_text=input_text,output_text=output_text)

@app.route("/")
def index():
    input_text="enter info:"
    output_text=""
    return render_template("index.html",input_text=input_text,output_text=output_text)
if __name__ == "__main__":
    app.run(debug=True)

