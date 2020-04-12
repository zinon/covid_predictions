# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics
- Last update: 2020-04-10 00:00:00
- Total confirmed cases: 1691719
- Total death cases: 102524
- Total active cases: 1247744
- Total recovered cases: 341451
- Death rate %: 6.06

 | Country        |   Confirmed |   Deaths |   Recovered |   Active |   Death Rate |   Recovery Rate |
|:---------------|------------:|---------:|------------:|---------:|-------------:|----------------:|
| US             |      496535 |    18586 |           0 |   477949 |      3.74314 |        0        |
| Spain          |      158273 |    16081 |       55668 |    86524 |     10.1603  |       35.1721   |
| Italy          |      147577 |    18849 |       30455 |    98273 |     12.7723  |       20.6367   |
| France         |      125931 |    13215 |       25195 |    87521 |     10.4938  |       20.007    |
| Germany        |      122171 |     2767 |       53913 |    65491 |      2.26486 |       44.1291   |
| Mainland China |       81907 |     3336 |       77472 |     1099 |      4.07291 |       94.5853   |
| UK             |       74605 |     8974 |         588 |    65043 |     12.0287  |        0.788151 |
| Iran           |       68192 |     4232 |       35465 |    28495 |      6.20601 |       52.0076   |
| Turkey         |       47029 |     1006 |        2423 |    43600 |      2.13911 |        5.15214  |
| Belgium        |       26667 |     3019 |        5568 |    18080 |     11.3211  |       20.8797   |


Rates are reported in percentage.

## Pies

### Confirmed Cases for Top Countries
![Pie confirmed](images/eda/pie_confirmed.png "Pie confirmed")

### Deaths for Top Countries
![Pie deaths](images/eda/pie_deaths.png "Pie deaths")


## Doubling Times for Confirmed Cases using exponential fits
The "doubling time" refers to the time it takes for a population to double in size.
When the relative growth rate
<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;k" />
for an exponentially growing population
<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;N(t)&space;=&space;N(0)e^{kt}" />
is constant over a time interval,
the quantity undergoes exponential growth and has a constant doubling time or period,
which can be calculated directly from the growth rate as follows
<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;T&space;=&space;\tfrac{\ln&space;2}{k}" />.
An increase in the epidemic or pandemic doubling time indicates a slowdown of the disease transmission.
In particular for he coronavirus pandemia, the bigger doubling time (measured in days)
the better is in terms of a slowingdown spread. Small values indicate steeply increasing populations.

Note: We assume that the outbreak in Europe occured around 10-15 February 2020.

### Time window - Last 15 days (10.04.2020)
|    | Country   |   Doubling Time |   Doubling Time Error |
|---:|:----------|----------------:|----------------------:|
|  2 | Italy     |        15.0291  |              0.685628 |
|  5 | Greece    |        11.2051  |              0.571117 |
|  0 | Germany   |         9.15512 |              0.535314 |
|  3 | Spain     |         8.925   |              0.560385 |
|  4 | France    |         6.17459 |              0.24088  |
|  6 | US        |         5.60267 |              0.237149 |
|  1 | UK        |         5.58755 |              0.206167 |


### Time window - Last 15 days (03.04.2020)
|    | Country   |   Doubling Time |   Doubling Time Error |
|---:|:----------|----------------:|----------------------:|
|  2 | Italy     |        10.2942  |              0.538543 |
|  5 | Greece    |         8.17605 |              0.194635 |
|  0 | Germany   |         6.34621 |              0.282157 |
|  4 | France    |         5.95507 |              0.193496 |
|  3 | Spain     |         5.8896  |              0.290198 |
|  1 | UK        |         4.42453 |              0.110834 |
|  6 | US        |         4.14469 |              0.164233 |

Note: China does not expose an exponential growth.

### Exponential Growth for Germany (Today)
![Germany's doubling time](images/doubling_time/Germany.png "Germany's doubling time")
Growth for Germany considering the last 15 days.

## Doubling Times for Confirmed Cases using gradients
The relative growth rate
<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;k" />
used in the calculation of the doubling time
<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;T&space;=&space;\tfrac{\ln&space;2}{k}" />.
is derived by dividing the exponential growth function
<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;f(t)k" />
to its the gradient (first derivative) 
<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;k=\tfrac{f^\prime(t)}{f(t)}k" />.

![Doubling times grad](images/doubling_time/pie_confirmed_gradients.png "Doubling times using gradients")

## Overview 
![Overview stats](images/eda/overview.png?raw=true "Overview")
Overview statistics for top affected countries.

## Global growth
![Global growth](images/eda/overall.png?raw=true "Global growth")
Global growth rate of confirmed cases.

## Leaders
![Leaders growth](images/eda/leaders.png?raw=true "Leaders growth")
Confirmed cases for the most affected countries and Germany.

## Mortality
![Mortality rate](images/eda/mortality.png?raw=true "Mortality rate")
Percentage mortality (death rate) for top affected countries and Germany.

## Death Rates - Head & Tail
![Death rate](images/eda/top_death_rates.png "Death rates")

## Percentage Rates
![Percentage Rates](images/eda/rates.png?raw=true "Percentage rates")
Percentage rates for deaths, recovered cases and confirmed cases on a global scale. Mainland China is included.

## Germany Overview
![Germany status](images/eda/Germany_view.png "Germany")

# Predictions with Facebook Prophet
Predictions are performed using an additive forecasting model

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;y(t)=g(t)&plus;s(t)&plus;h(t)&plus;\epsilon_t" />

where
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;g(t)" /> represents the trend
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;s(t)" /> the periodic component
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;h(t)" /> holiday related events
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\epsilon_t" /> the error.

The data are provided on a daily basis.
Also, the current model is not aware of holidays.

Prophet allows you to make forecasts using a logistic growth trend model,
with a specified carrying capacity which is indicated by a horizontal dashed line in each of the plots.

## Predictions for confirmed cases

### Linear model
#### Global
![linear confirmed](images/predictions/prophet_linear_confirmed_prediction.png)

#### Germany
![linear confirmed germany](images/predictions/prophet_linear_confirmed_Germany_prediction.png)

### Logistic model
#### Global
![log confirmed](images/predictions/prophet_logistic_confirmed_prediction.png)

#### Germany
![log confirmed germany](images/predictions/prophet_logistic_confirmed_Germany_prediction.png)

## Predictions for death cases

### Linear model
#### Global
![linear deaths](images/predictions/prophet_linear_deaths_prediction.png)

#### Germany
![linear deaths germany](images/predictions/prophet_linear_deaths_Germany_prediction.png)

### Logistic model
#### Global
![log deaths](images/predictions/prophet_logistic_deaths_prediction.png)

#### Germany
![lin germany deaths](images/predictions/prophet_logistic_deaths_Germany_prediction.png)

## Predictions for active cases

### Linear model
#### Global
![linear active](images/predictions/prophet_linear_active_prediction.png)

### Logistic model
#### Global
![log active](images/predictions/prophet_logistic_active_prediction.png)

## Predictions for recovered cases

### Linear model
#### Global
![linear recovered](images/predictions/prophet_linear_recovered_prediction.png)

### Logistic model
#### Global
![log recovered](images/predictions/prophet_logistic_recovered_prediction.png)


## Predictions for mortality rate
#### Global
![linear mortality](images/predictions/prophet_linear_mortality_prediction.png)

#### Germany
![linear mortality germany](images/predictions/prophet_linear_mortality_Germany_prediction.png)

# Predictions with ARIMA
## Confirmed Cases
### Global 
#### Train - Prediction - Validation
![train prediction validation](images/predictions/arima_train_valid_pred.png)

#### Auto-corellation 
![auto correlation](images/predictions/arima_auto_correlation.png)

# Predictions with Auto ARIMA
## Confirmed Cases
### Global
![auto arima confirmed global](images/predictions/auto_arima_forecast.png)

### Germany
![auto arima confirmed](images/predictions/auto_arima_forecast_Germany.png)

# Factor Analysis

## Logistic function
The spread of infectious disease can be modeled using a logistic curve rather than an exponential curve or a linear function. The growth starts exponentially, but must slow down after some point called the inflection point. The inflection point is essentially the midpoint of the spread. We attempt to model the number of COVID-19 cases using a logistic curve.

![logistic function](images/theory/logfn_ext.png)

A logistic function or logistic curve is a common S-shaped curve (sigmoid curve) with equation


<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;f(t)=\frac{L}{1&plus;e^{-k(t-t_0)}}" />

where

- <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;t" /> = the time variable
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;t_0" /> = the sigmoid's midpoint / inflection point 
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;L" /> = the curve's maximum value (plateau)
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;k"/> = the logistic growth rate or steepness of the curve


The following growth metrics can be considered for the confirmed cases for each country:

* Growth Factor =  <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\frac{\Delta&space;L_i&space;}{\Delta&space;L_{i-1}&space;}" /> with i=days, weeks, months, ...
* Growth Ratio
* Growth Rate
* 2nd Derivative

These growth metrics can be explored to gain insight into which countries may have already hit their inflection points.
For example, if a country's growth factor has stabilized around 1.0 then this can be a sign that that country has reached it's inflection point.  When fitting data with a logistic function, we may predict if a country has hit their inflection point, and therefore we can predict when they will reach a possible maximum number of confirmed cases.




