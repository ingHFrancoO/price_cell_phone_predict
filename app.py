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
    # print("request")
    # print(request.form)
    if request.method == 'POST':

        battery_power    =   int(request.form['battery_power'])
        fc               =   int(request.form['fc'])
        pc               =   int(request.form['pc'])
        ram              =   int(request.form['ram'])
        int_memory       =   int(request.form['int_memory'])
        n_cores          =   int(request.form['n_cores'])
        clock_speed      =   float(request.form['clock_speed'])
        px_height        =   int(request.form['px_height'])
        px_width         =   int(request.form['px_width'])
        mobile_wt        =   int(request.form['mobile_wt'])
        sc_h             =   int(request.form['sc_h'])
        sc_w             =   int(request.form['sc_w'])
        talk_time        =   int(request.form['talk_time'])
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
            'blue': blue, 
            'fc':fc, 
            'm_dep':pc,
            'dual_sim':dual_sim, 
            'three_g':three_g, 
            'four_g':four_g, 
            'touch_screen':touch_screen,
            'wifi':wifi, 
            'battery_power':battery_power, 
            'clock_speed':clock_speed,
            'int_memory':int_memory, 
            'mobile_wt':mobile_wt, 
            'n_cores':n_cores, 
            # 'pc':pc,
            'px_height':px_height, 
            'px_width':px_width, 
            'ram':ram, 
            'sc_h':sc_h, 
            'sc_w':sc_w, 
            'talk_time':talk_time
        }]

        # movile = [{
        #     'blue': True, 
        #     'pc ': 20, 
        #     'm_dep':0.1,
        #     'dual_sim': True, 
        #     'three_g': True, 
        #     'four_g': True, 
        #     'touch_screen': True,
        #     'wifi': True, 
        #     'battery_power': 1900, 
        #     'clock_speed': 3.0,
        #     'int_memory': 64, 
        #     'mobile_wt': 200, 
        #     'n_cores': 6, 
        #     # 'pc ': 10,
        #     'px_height': 1960, 
        #     'px_width': 1800, 
        #     'ram': 3998, 
        #     'sc_h': 13, 
        #     'sc_w': 10, 
        #     'talk_time': 20
        # }]

        price = str(predecir_price( movile ))
        print("price " + price)

        return render_template('index.html', price=price, data=request.form)
    else:
        return render_template('index.html')


if __name__ == '__main__':
  app.run(host="0.0.0.0")

