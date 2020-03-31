# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics

- Last update: 2020-03-30 00:00:00
- Total confirmed cases: 782365
- Total death cases: 37581
- Total active cases: 586328
- Total recovered cases: 158456
- Death rate %: 4.80

 | Country        |   Confirmed |   Deaths |   Recovered |   Active |   Death Rate |   Recovery Rate |
|:---------------|------------:|---------:|------------:|---------:|-------------:|----------------:|
| US             |      161807 |     2978 |           0 |   158829 |     1.84046  |        0        |
| Italy          |      101739 |    11591 |       14620 |    75528 |    11.3929   |       14.3701   |
| Spain          |       87956 |     7716 |       16780 |    63460 |     8.77257  |       19.0777   |
| Mainland China |       81478 |     3304 |       75790 |     2384 |     4.05508  |       93.019    |
| Germany        |       66885 |      645 |       13500 |    52740 |     0.964342 |       20.1839   |
| France         |       45170 |     3030 |        7964 |    34176 |     6.70799  |       17.6312   |
| Iran           |       41495 |     2757 |       13911 |    24827 |     6.64417  |       33.5245   |
| UK             |       22453 |     1411 |         171 |    20871 |     6.28424  |        0.761591 |
| Switzerland    |       15922 |      359 |        1823 |    13740 |     2.25474  |       11.4496   |
| Belgium        |       11899 |      513 |        1527 |     9859 |     4.31129  |       12.833    |

Rates are reported in percentage.

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

## Percentage Rates
![Percentage Rates](images/eda/rates.png?raw=true "Percentage rates")
Percentage rates for deaths, recovered cases and confirmed cases on a global scale. Mainland China is included.

# Predictions with Facebook Prophet

Predictions are performed using an additive forecasting model

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;y(t)=g(t)&plus;s(t)&plus;h(t)&plus;\epsilon_t" />

where
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;g(t)"> represents the trend
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;s(t)" /> the periodic component
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;h(t)" /> holiday related events
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\epsilon_t" /> the error.

The data are provided on a daily basis.
Also, the current model is not aware of holidays.

Prophet allows you to make forecasts using a logistic growth trend model, with a specified carrying capacity which is indicated by a horizontal dashed line in each of the plots.

## Predictions for global confirmed cases

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

## Predictions for global death cases

### Linear model
![linear deaths](images/predictions/prophet_linear_deaths_prediction.png)

### Logistic model
![log deaths](images/predictions/prophet_logistic_deaths_prediction.png)

## Predictions for global active cases

### Linear model
![linear active](images/predictions/prophet_linear_active_prediction.png)

### Logistic model
![log active](images/predictions/prophet_logistic_active_prediction.png)

## Predictions for global recovered cases

### Linear model
![linear recovered](images/predictions/prophet_linear_recovered_prediction.png)

### Logistic model
![log recovered](images/predictions/prophet_logistic_recovered_prediction.png)


## Predictions for global mortality rate
![linear mortality](images/predictions/prophet_linear_mortality_prediction.png)

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




