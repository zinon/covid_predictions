# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics
- Last update: 2020-04-19 00:00:00
- Total confirmed cases: 2401379
- Total death cases: 165044
- Total active cases: 1694616
- Total recovered cases: 541719
- Death rate %: 6.87

 | Country        |   Confirmed |   Deaths |   Recovered |   Active |   Death Rate |   Recovery Rate |
|:---------------|------------:|---------:|------------:|---------:|-------------:|----------------:|
| US             |      759086 |    40661 |           0 |   718425 |     5.35657  |        0        |
| Spain          |      198674 |    20453 |       77357 |   100864 |    10.2948   |       38.9366   |
| Italy          |      178972 |    23660 |       47055 |   108257 |    13.2199   |       26.2918   |
| France         |      154097 |    19744 |       37183 |    97170 |    12.8127   |       24.1296   |
| Germany        |      145184 |     4586 |       88000 |    52598 |     3.15875  |       60.6127   |
| UK             |      121172 |    16095 |         436 |   104641 |    13.2828   |        0.359819 |
| Turkey         |       86306 |     2017 |       11976 |    72313 |     2.33703  |       13.8762   |
| Mainland China |       82735 |     4632 |       77068 |     1035 |     5.5986   |       93.1504   |
| Iran           |       82211 |     5118 |       57023 |    20070 |     6.22544  |       69.3618   |
| Russia         |       42853 |      361 |        3291 |    39201 |     0.842415 |        7.67974  |


Rates are reported in percentage.

## Pies

### Confirmed Cases for Top Countries
![Pie confirmed](images/eda/pie_confirmed.png "Pie confirmed")

### Deaths for Top Countries
![Pie deaths](images/eda/pie_deaths.png "Pie deaths")

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
### Cases overview
![Germany status](images/eda/Germany_view.png "Germany overview")

### Daily confirmed cases
![Germany daily cases](images/eda/daily_confirmed_germany.png "Germany daily cases")

# Predictions with Facebook Prophet
Predictions are performed using an additive forecasting model

<img src="https://render.githubusercontent.com/render/math?math=y(t) = g(t) %2B s(t) %2B \epsilon_t">

where
- <img src="https://render.githubusercontent.com/render/math?math=g(t)" /> represents the trend
- <img src="https://render.githubusercontent.com/render/math?math=s(t)" /> the periodic component
- <img src="https://render.githubusercontent.com/render/math?math=h(t)" /> holiday related events
- <img src="https://render.githubusercontent.com/render/math?math=\epsilon_t" /> the error.

The data are provided on a daily basis. Also, the current model is not aware of holidays.

Prophet allows you to make forecasts using a logistic growth trend model,
with a specified carrying capacity which is indicated by a horizontal dashed line in each of the plots.

## Predictions for Confirmed cases

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

## Predictions for Death cases

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

## Predictions for Mortality
#### Global
![linear mortality](images/predictions/prophet_linear_mortality_prediction.png)

#### Germany
![linear mortality germany](images/predictions/prophet_linear_mortality_Germany_prediction.png)

## Predictions for Active cases
### Linear model
#### Global
![linear active](images/predictions/prophet_linear_active_prediction.png)

### Logistic model
#### Global
![log active](images/predictions/prophet_logistic_active_prediction.png)

## Predictions for Recovered cases
### Linear model
#### Global
![linear recovered](images/predictions/prophet_linear_recovered_prediction.png)

### Logistic model
#### Global
![log recovered](images/predictions/prophet_logistic_recovered_prediction.png)

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

## Doubling Times for Confirmed Cases using exponential fits
The "doubling time" refers to the time it takes for a population to double in size.
When the relative growth rate
<img src="https://render.githubusercontent.com/render/math?math=k" />
for an exponentially growing population
<img src="https://render.githubusercontent.com/render/math?math=N(t)=N(0)e^{kt}" />
is constant over a time interval,
the quantity undergoes exponential growth and has a constant doubling time or period,
which can be calculated directly from the growth rate as follows
<img src="https://render.githubusercontent.com/render/math?math=T=\tfrac{\ln 2}{k}" />.
An increase in the epidemic or pandemic doubling time indicates a slowdown of the disease transmission.
In particular for he coronavirus pandemia, the bigger doubling time (measured in days D)
the better is in terms of a slowingdown spread. Small values indicate steeply increasing populations.

Note: We assume that the outbreak in Europe occured around 10-15 February 2020.

### Time window - Last 15 days (19.04.2020)
|    | Country   |   Doubling Time |   Doubling Time Error |
|---:|:----------|----------------:|----------------------:|
|  5 | Greece    |         35.9963 |              2.95836  |
|  2 | Italy     |         29.2174 |              0.715912 |
|  0 | Germany   |         26.551  |              1.36846  |
|  3 | Spain     |         24.2667 |              0.724882 |
|  4 | France    |         21.7853 |              1.7145   |
|  6 | US        |         12.5207 |              0.444251 |
|  1 | UK        |         10.9005 |              0.425185 |


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
The relative growth rate <img src="https://render.githubusercontent.com/render/math?math=k" /> used in the calculation of the doubling time

<img src="https://render.githubusercontent.com/render/math?math=T=\tfrac{\ln 2}{k}" />

is derived by dividing the exponential growth function

<img src="https://render.githubusercontent.com/render/math?math=f(t)=e^{kt}" />

to its the gradient (first derivative) 

<img src="https://render.githubusercontent.com/render/math?math=k=\tfrac{f^\prime(t)}{f(t)}" />.

![Doubling times grad](images/doubling_time/pie_confirmed_gradients.png "Doubling times using gradients")

## Logistic function
The spread of infectious disease can be modeled using a logistic curve rather than an exponential curve or a linear function. The growth starts exponentially, but must slow down after some point called the inflection point. The inflection point is essentially the midpoint of the spread. We attempt to model the number of COVID-19 cases using a logistic curve.

![logistic function](images/theory/logfn_ext.png)

A logistic function or logistic curve is a common S-shaped curve (sigmoid curve) with equation

<img src="https://render.githubusercontent.com/render/math?math=f(t)=\frac{L}{1 %2B e^{-k(t-t_0)}}" />

where

- <img src="https://render.githubusercontent.com/render/math?math=t" /> = the time variable
- <img src="https://render.githubusercontent.com/render/math?math=t_0" /> = the sigmoid's midpoint / inflection point 
- <img src="https://render.githubusercontent.com/render/math?math=L" /> = the curve's maximum value (plateau)
- <img src="https://render.githubusercontent.com/render/math?math=k"/> = the logistic growth rate or steepness of the curve


The following growth metrics can be considered for the confirmed cases for each country:

* <img src="https://render.githubusercontent.com/render/math?math=\text{Growth Factor}=\tfrac{\Delta L_i}{\Delta L_{i-1}}" /> with <img src="https://render.githubusercontent.com/render/math?math=i" /> = days, weeks, months, ...
* Growth Ratio
* Growth Rate
* 2nd Derivative

These growth metrics can be explored to gain insight into which countries may have already hit their inflection points.
For example, if a country's growth factor has stabilized around 1.0 then this can be a sign that that country has reached it's inflection point.  When fitting data with a logistic function, we may predict if a country has hit their inflection point, and therefore we can predict when they will reach a possible maximum number of confirmed cases.


## Factor analysis for Germany

### Growth rate
![GR](images/factor_analysis/growth_rate2_Germany.png)

The growth rate or first derivative on logarithmus of the exponential growth function gives the constant k that appears in the exponential function.

### Doubling time
![DT](images/factor_analysis/doubling_time_Germany.png)

The doubling time is calulcated by dividing
 <img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;\ln(2)" />
to the constant
<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;k" />.

### Growth factor
![GF](images/factor_analysis/growth_factor_Germany.png)

The growth factor on day D is the number of confirmed cases on day D minus confirmed cases on day D-1 divided by the number of confirmed cases on day D-1 minus confirmed cases on day D-2.

### Growth ratio
![GRat](images/factor_analysis/growth_ratio_Germany.png)

The growth ratio on day D is the number of confirmed cases on day D divided by the number of confirmed cases on day D-1.

### Second derivative of exponential growth
![2ndDer](images/factor_analysis/second_derivative_Germany.png)
