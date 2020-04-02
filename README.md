# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics

- Total confirmed cases: 932605
- Total death cases: 46808
- Total active cases: 702418
- Total recovered cases: 183379
- Death rate %: 5.02

 | Country        |   Confirmed |   Deaths |   Recovered |   Active |   Death Rate |   Recovery Rate |
|:---------------|------------:|---------:|------------:|---------:|-------------:|----------------:|
| US             |      213372 |     4757 |           0 |   208615 |      2.22944 |        0        |
| Italy          |      110574 |    13155 |       16847 |    80572 |     11.897   |       15.236    |
| Spain          |      104118 |     9387 |       22647 |    72084 |      9.01573 |       21.7513   |
| Mainland China |       81555 |     3312 |       76248 |     1995 |      4.06106 |       93.4927   |
| Germany        |       77872 |      920 |       18700 |    58252 |      1.18143 |       24.0138   |
| France         |       57749 |     4043 |       11053 |    42653 |      7.00099 |       19.1397   |
| Iran           |       47593 |     3036 |       15473 |    29084 |      6.37909 |       32.5111   |
| UK             |       29865 |     2357 |         179 |    27329 |      7.89218 |        0.599364 |
| Switzerland    |       17768 |      488 |        2967 |    14313 |      2.74651 |       16.6986   |
| Turkey         |       15679 |      277 |         333 |    15069 |      1.76669 |        2.12386  |


Rates are reported in percentage.

## Doubling Times for Confirmed Cases

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

We assume that the outbreak in Europe occured around 10-15 February 2020.

### 15 February - Today
|    | Country   |   Doubling Time |   Doubling Time Error |
|---:|:----------|----------------:|----------------------:|
|  2 | Italy     |         6.81088 |             0.244844  |
|  5 | Greece    |         6.45466 |             0.248195  |
|  4 | France    |         5.02641 |             0.11177   |
|  0 | Germany   |         4.82211 |             0.137639  |
|  3 | Spain     |         4.59738 |             0.120638  |
|  1 | UK        |         3.88707 |             0.0610509 |
|  6 | US        |         3.43474 |             0.0820507 |


### 15 February - 31 March 2020
|    | Country   |   Doubling Time |   Doubling Time Error |
|---:|:----------|----------------:|----------------------:|
|  2 | Italy     |         6.50204 |             0.220959  |
|  5 | Greece    |         6.20843 |             0.240083  |
|  4 | France    |         4.82414 |             0.100359  |
|  0 | Germany   |         4.55695 |             0.116807  |
|  3 | Spain     |         4.34995 |             0.101768  |
|  1 | UK        |         3.71551 |             0.0476741 |
|  6 | US        |         3.22256 |             0.0693933 |


### 15 February - 15 March 2020
|    | Country        |   Doubling Time |   Doubling Time Error |
|---:|:---------------|----------------:|----------------------:|
|  8 | South Korea    |         7.92763 |             0.817927  |
|  9 | Iran           |         4.46828 |             0.250423  |
|  2 | Italy          |         3.6665  |             0.102771  |
|  5 | Greece         |         2.87314 |             0.214048  |
|  4 | France         |         2.77615 |             0.0915842 |
|  1 | UK             |         2.61483 |             0.130392  |
|  6 | US             |         2.54253 |             0.0432671 |
|  0 | Germany        |         2.5209  |             0.0961247 |
|  3 | Spain          |         1.88386 |             0.0955873 |

Note: China does not expose an exponential growth.

### Germany Today
![Germany's doubling time](images/doubling_time/Germany.png "Germany's doubling time")

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
- <img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;g(t)" /> represents the trend
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




