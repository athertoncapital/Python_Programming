__author__ = 'William_Chuang'


from flask import Flask
from flask import request
import conversions

app = Flask(__name__)
app.debug=True

@app.route('/')
@app.route('/', methods=['POST'])
def hello_world():
    html = ''
    html += '<html>\n'
    html += '<title>\n'
    html += 'Hi\n'
    html += '</title>'
    ###############################_above the body_###############################
    html +='<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' #Specifies the character encoding for the document.

    #html += '<style>'
    #html += 'body {'
    #html += 'background-color: #b0c4de;'
    #html += '}'

    #Originally, I putted "<link rel="stylesheet" type="text/css" href="/static/css.css" media="screen" />" here, and it didn't work.

    #html += '</style>\n'

    html += '<link rel="stylesheet" type="text/css" href="/static/css.css" media="screen" />' #should be outside the <style>
    #################################_above the body_###############################
    html += '<body>\n'
    html +='<div id="container">'

    html +='<div id="header">'
    html +='<div class="headtitle">Hi, here is my first python web app project!</div>'
    html +='</div>'

    html +='<div id="menu">'
    html +='<ul>'
    html +='<li><a href="/" title="">HOME</a></li>'
    html +='</ul>'
    html +='</div>'

    html +='<div id="content">'
    html +='<div id="insidecontent"> <br>'
    #########################

    html += '<h1>\n'
    html += 'William Huanshan Chuang\n'
    html += '</h1>\n'
    html += '<p>\n'
    html += '<br>\n'
    html += '<p>\n'
    html += '<h3>Here are my three favorite links:</h3>\n'
    html += '</p>\n'
    html += '<p>\n'
    html += 'Coursera\n'
    html += '</p>\n'
    html += '<a href="https://www.coursera.org/">https://www.coursera.org/</a>\n'
    html += '<p>\n'
    html += 'edX\n'
    html += '</p>\n'
    html += '<a href="https://www.edx.org/">https://www.edx.org/</a>\n'
    html += '<p>\n'
    html += 'Udacity\n'
    html += '</p>\n'
    html += '<a href="https://www.udacity.com/">https://www.udacity.com/</a>\n'
    html += '</p>\n'
    html += '<p>\n'
    html += '<br>\n'
    html += '<br>\n'
    html += '<h3>Conversion Tools:</h2>\n'
    html += '<form action="Conversion_tools" method="POST" >\n'
    html += 'Start value: <input type="text" name="start_value" />\n'
    html += '</p>\n'
    html += '<p>\n'
    html += 'End value: <input type="text" name="end_value" />\n'
    html += '</p>\n'
    html += '<p>\n'
    html += 'Step value: <input type="text" name="step_value" />\n'
    html += '</p>\n'
    html += '<p>\n'
    html += 'End value must larger than start value.\n'
    html += '</p>\n'
    html += '<p>\n'
    #html += '<form>'
    html += 'What kind of conversions you would like to make?\n'
    html += '<p>\n'
    html += '<input type="radio" name="conversion" value="inches_to_centimeters">\n'
    html += 'inches to centimeters\n'
    html += '<br>\n'
    html += '<p>\n'
    html += '<input type="radio" name="conversion" value="centimeters_to_inches">\n'
    html += 'centimeters to inches\n'
    html += '<br>\n'
    html += '<p>\n'
    html += '<input type="radio" name="conversion" value="Fahrenheit_to_Celsius">\n'
    html += 'Fahrenheit to Celsius\n'
    html += '<br>\n'
    html += '<p>\n'
    html += '<input type="radio" name="conversion" value="Celsius_to_Fahrenheit">\n'
    html += 'Celsius to Fahrenheit\n'
    html += '<br>\n'
    html += '<p>\n'
    html += '<input type="radio" name="conversion" value="bytes_to_kilobytes">\n'
    html += 'bytes to kilobytes\n'
    html += '<br>\n'
    html += '<p>\n'
    html += '<input type="radio" name="conversion" value="kilobytes_to_bytes">\n'
    html += 'Inches to Centimeters\n'
    html += '<br>\n'
    html += '<p>\n'
    html += '<input type="radio" name="conversion" value="bytes_to_megabytes">\n'
    html += 'bytes to megabytes\n'
    html += '<br>\n'
    html += '<p>\n'
    html += '<input type="radio" name="conversion" value="megabytes_to_bytes">\n'
    html += 'megabytes to bytes\n'
    html += '<br>\n'
    html += '<p>'
    #html += '<input type="submit" />'
    #html += '</form>'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'  # button
    html += '</form>\n'

    html +='<div style="clear: both;"></div>'
    html +='<div id="footer"> <span>Copyright © 2015 | All Rights Reserved  </span>'
    html +='</div>'

    html +='</div>'
    html +='</div>'
    html += '</body>\n'
    html += '</html>\n'
    return html

@app.route('/Conversion_tools', methods=['POST'])
def Conversion_tools():
    start_value = request.form['start_value']
    end_value = request.form['end_value']
    step_value = request.form['step_value']
    conversion = request.form['conversion']
    v="N/A"
    r="N/A"
    if conversion =="inches_to_centimeters":
        v="(Inches)"
        r="(Centimeters)"
    elif conversion =="centimeters_to_inches":
        v="(Centimeters)"
        r="(Inches)"
    elif conversion =="Fahrenheit_to_Celsius":
        v="(Fahrenheit)"
        r="(Celsius)"
    elif conversion =="Celsius_to_Fahrenheit":
        v="(Celsius)"
        r="(Fahrenheit)"
    elif conversion =="bytes_to_kilobytes":
        v="(bytes)"
        r="(kilobytes)"
    elif conversion =="kilobytes_to_bytes":
        v="(kilobytes)"
        r="(bytes)"
    elif conversion =="bytes_to_megabytes":
        v="(bytes)"
        r="(megabytes)"
    elif conversion =="megabytes_to_bytes":
        v="(megabytes)"
        r="(bytes)"

    html = ''
    html += '<!DOCTYPE html>'
    html += '<html>\n'
    #html += '<style>'
    #html += 'body {'
    #html += 'background-color: green;'
    #html += '}'
    #html += ' p {'
    #html += 'color: rgb(191, 0, 255);'
    #html += '}'
    #html += '</style>'
    html += '<title>\n'
    html += 'Conversion Results\n'
    html += '</title>'
    html +='<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' #Specifies the character encoding for the document.
    html += '<link rel="stylesheet" type="text/css" href="/static/css.css" media="screen" />'

    html += '<body>\n'
    html +='<div id="container">'

    html +='<div id="header">'
    html +='<div class="headtitle">Here you are!</div>'
    html +='</div>'

    html +='<div id="menu">'
    html +='<ul>'
    html +='<li><a href="/" title="">HOME :)</a></li>'
    html +='</ul>'
    html +='</div>'

    html +='<div id="content2">'
    html +='<div id="insidecontent"> <br>'
    html += '<table border="1">\n'
    html += '<tr>'
    html += '<td>'
    html += 'Input'+str(v)
    html += '</td>'
    html += '<td>'
    html += 'Result'+str(r)
    html += '</td>'
    html += '</tr>'
    i = int(start_value)
    while i <= int(end_value):
        html += '<tr>'
        html += '<th>'
        html += str(i)
        html += '</th>'
        html += '<td>'
        html += str(conversions.formula(conversion,i))
        html += '</td>'
        html += '</tr>'
        i += int(step_value)
    html += '</table>\n'
    html += '<form action="/" method="POST" >\n'
    html += '<input type="submit" value="Try Again (by home decorator! Or, u can click HOME in the main menu! :) )" />\n'  # button
    html += '</form>\n'
    html += '<button onclick="goBack()">Have some typos or just wanna do some slightly changes on your inputs? Then, we can back by the history!!</button>'
    html += '<script>'
    html += 'function goBack() {'
    html += 'window.history.back();'
    html += '}\n'
    html += '</script>\n'
    #html += '<FORM><INPUT Type="button" VALUE="Click here if you have some typos! , Another method by using history.)" onClick="history.go(-1);return true;"></FORM>'


    html +='<div style="clear: both;"></div>'
    html +='<div id="footer"> <span>Copyright © 2015 | All Rights Reserved  </span>'
    html +='</div>'

    html +='</div>'
    html +='</div>'
    html += '<body>\n'

    html += '<html>\n'
    return html



#if __name__ == '__main__':
app.run()
