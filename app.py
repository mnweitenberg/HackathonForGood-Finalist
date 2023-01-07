from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from functions import compute_tomato, compute_cucumber, compute_electricity_light, \
	compute_electricity_heating, compute_gas_expenses, \
	compute_old_emisions, compute_recoupment

app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

@app.route('/')
def input():
	return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
	total_investment 			= 45000
	percentage_heat_pump 		= 0.11
	percentage_heat_net 		= 0.07
	percentage_solar_panels 	= 0.15
	percentage_gas				= 1 - percentage_heat_pump - percentage_heat_net - percentage_solar_panels
	cucumber					= compute_cucumber(request.form['cucumber'])
	cucumber_lights 			= compute_electricity_light(request.form['cucumber'])
	cucumber_heat 				= compute_electricity_heating(request.form['cucumber'])
	tomato						= compute_tomato(request.form['tomato'])
	tomato_lights 				= compute_electricity_light(request.form['tomato'])
	tomato_heat 				= compute_electricity_heating(request.form['tomato'])
	total_energy 				= cucumber_lights + cucumber_heat + tomato_lights + tomato_heat
	gas_energy					= round(total_energy * percentage_gas)
	heat_pump_energy			= round(total_energy * percentage_heat_pump)
	heat_net_energy				= round(total_energy * percentage_heat_net)
	solar_energy				= round(total_energy * percentage_solar_panels)
	current_expenses 			= compute_gas_expenses(total_energy)
	future_expenses 			= compute_gas_expenses(total_energy * percentage_gas)
	future_expenses_percentage 	= round(future_expenses / current_expenses * 100)
	savings						= round(current_expenses - future_expenses)
	recoupment 					= compute_recoupment(current_expenses, total_investment, future_expenses)
	old_emissions 				= compute_old_emisions(total_energy)
	future_emission				= round(old_emissions * percentage_gas)
	co_reduction				= round(100 - future_emission / old_emissions * 100)
	return render_template('results.html', 
		company						= request.form['company'], 
		cucumber 					= "{:,}".format(cucumber),
		cucumber_lights				= "{:,}".format(cucumber_lights),
		cucumber_heat				= "{:,}".format(cucumber_heat),
		tomato 						= "{:,}".format(tomato),
		tomato_lights				= "{:,}".format(tomato_lights),
		tomato_heat					= "{:,}".format(tomato_heat),
		gas_energy					= "{:,}".format(gas_energy),
		heat_pump_energy			= "{:,}".format(heat_pump_energy),
		heat_net_energy				= "{:,}".format(heat_net_energy),
		solar_energy				= "{:,}".format(solar_energy),
		total_energy 				= "{:,}".format(total_energy),
		current_expenses 			= "{:,}".format(current_expenses),
		future_expenses 			= "{:,}".format(future_expenses),
		future_expenses_percentage 	= "{:,}".format(future_expenses_percentage),
		savings 					= "{:,}".format(savings),
		savings_percentage 			= "{:,}".format(savings / current_expenses * 100),
		total_investment 			= "{:,}".format(total_investment),
		recoupment 					= "{:,}".format(recoupment),
		old_emissions 				= "{:,}".format(old_emissions),
		future_emission 			= "{:,}".format(future_emission),
		future_emission_percentage	= "{:,}".format(percentage_gas * 100),
		co_reduction				= "{:,}".format(co_reduction),
		)

if __name__ == '__main__':
   app.run(debug = True)