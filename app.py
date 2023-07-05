#write python flask input form, with input textbox, checkbox to select options,  output texbox, submit button
from flask import Flask, render_template, request
import os
from backend.property_llm import predict_llm_property
app = Flask(__name__)

@app.route("/")
def index():
    # Get the input from the user
    input_text = request.form.get("input_text")
    option_text = request.form['options']
    
    # Generate the output text
    #output_text = "You entered: " + input_text
    #for option in options:
    #    output_text += "\nYou selected: " + option

    # Render the template



    output_text=predict_llm_property(input_text)
    return render_template("index.html", input_text=input_text, options=option_text, output_text=output_text)

if __name__ == "__main__":
    app.run(debug=True)

