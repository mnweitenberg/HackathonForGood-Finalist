import math

tomato_yield_per_square_meter = 30
def compute_tomato(cube_meters):
	output = int(cube_meters) * tomato_yield_per_square_meter
	return (output)

cucumber_yield_per_square_meter = 25
def compute_cucumber(cube_meters):
	output = int(cube_meters) * cucumber_yield_per_square_meter
	return (output)

kilowatt_lighting_per_square_meter = 0.01
daily_hours_of_lighting = 12
days_per_year = 365
greenhouse_heigth_in_meters = 5
def compute_electricity_light(cube_meters):
	output = int(cube_meters) / greenhouse_heigth_in_meters * kilowatt_lighting_per_square_meter \
		* daily_hours_of_lighting * days_per_year
	return (round(output))

# https://www.rapidtables.com/convert/power/BTU_to_kW.html
celcius_inside_temperature_in_winter = 15
celcius_outside_temperature_in_winter = -5
heat_transfer_coefficient = 1
btu_kw_factor = 3412
def compute_electricity_heating(cube_meters):
	temperature_difference = celcius_inside_temperature_in_winter - celcius_outside_temperature_in_winter
	length_of_sides = math.sqrt(int(cube_meters) / greenhouse_heigth_in_meters)
	surface_area = 4 * length_of_sides * greenhouse_heigth_in_meters + length_of_sides * length_of_sides
	btu = heat_transfer_coefficient * surface_area * temperature_difference
	output = btu / btu_kw_factor * 24 * days_per_year
	return ((round(output)))

natural_gas_price_per_kwh = 0.2889
def compute_gas_expenses(total_energy):
	return (round(natural_gas_price_per_kwh * total_energy))

def compute_recoupment(current_expenses, acquisition_costs, future_expenses):
	savings = current_expenses - future_expenses
	return (round(acquisition_costs / savings))

# https://www.quora.com/How-many-cubic-meters-of-natural-gas-do-we-need-to-produce-1-kWh-of-electricity?share=1
# https://www.globalpetrolprices.com/Netherlands/natural_gas_prices/natural_gas_to_produce_1kwh = 1000 / 35.315
cubic_meters_natural_gas_needed_for_1kwh = 0.32
co2_emission_per_cubic_meter_natural_gas = 2.2
def compute_old_emisions(total_energy):
	cubic_meter_natural_gas = cubic_meters_natural_gas_needed_for_1kwh * total_energy
	return (round(cubic_meter_natural_gas * co2_emission_per_cubic_meter_natural_gas))
	


