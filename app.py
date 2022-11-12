import sys
import pandas as pd
from joblib import load
from flask import Flask, render_template, url_for, request, redirect

MODELO = load('RF_final_model.joblib')
app = Flask(__name__, template_folder='template')

def predecir_price(movile):
	y2_pred = MODELO.predict( pd.DataFrame(movile) )
	return y2_pred


@app.route('/', methods=['POST', 'GET'])
def index():
    print("request")
    print(request.form)
    if request.method == 'POST':
        battery_power    =   float(request.form['battery_power'])
        fc               =   float(request.form['fc'])
        pc               =   float(request.form['pc'])
        ram              =   float(request.form['ram'])
        int_memory       =   float(request.form['int_memory'])
        n_cores          =   int(request.form['n_cores'])
        clock_speed      =   float(request.form['clock_speed'])
        px_height        =   float(request.form['px_height'])
        px_width         =   float(request.form['px_width'])
        mobile_wt        =   float(request.form['mobile_wt'])
        sc_h             =   float(request.form['sc_h'])
        sc_w             =   float(request.form['sc_w'])
        talk_time        =   float(request.form['talk_time'])
        # blue             =   bool(request.form['blue'])
        # dual_sim         =   bool(request.form['dual_sim'])
        # four_g           =   bool(request.form['four_g'])
        # three_g          =   bool(request.form['three_g'])
        # touch_screen     =   bool(request.form['touch_screen'])
        # wifi             =   bool(request.form['wifi'])

        blue             =   True
        dual_sim         =   True
        four_g           =   True
        three_g          =   True
        touch_screen     =   True
        wifi             =   True

        movile = [{
            'blue': blue, 'dual_sim':dual_sim, 'three_g':three_g, 'four_g':four_g, 'touch_screen':touch_screen,
            'wifi':wifi, 'battery_power':battery_power, 'battery_power':battery_power, 'clock_speed':clock_speed,
            'fc':fc, 'int_memory':int_memory, 'mobile_wt':mobile_wt, 'n_cores':n_cores, 'pc':pc,
            'px_height':px_height, 'px_width':px_width, 'ram':ram, 'sc_h':sc_h, 'sc_w':sc_w, 'talk_time':talk_time
        }]

        price = str(predecir_price( movile ))
        print("price " + str(price) )

        return render_template('index.html', price=price)
    else:
        return render_template('index.html')


if __name__ == '__main__':
  app.run(host="0.0.0.0")

