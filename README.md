# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics

- Last update: 2020-04-02 00:00:00
- Total confirmed cases: 1013157
- Total death cases: 52982
- Total active cases: 760648
- Total recovered cases: 199527
- Death rate %: 5.23

 | Country        |   Confirmed |   Deaths |   Recovered |   Active |   Death Rate |   Recovery Rate |
|:---------------|------------:|---------:|------------:|---------:|-------------:|----------------:|
| US             |      243453 |     5926 |           0 |   237527 |      2.43415 |        0        |
| Italy          |      115242 |    13915 |       18278 |    83049 |     12.0746  |       15.8605   |
| Spain          |      112065 |    10348 |       26743 |    74974 |      9.23393 |       23.8638   |
| Germany        |       84794 |     1107 |       22440 |    61247 |      1.30552 |       26.4641   |
| Mainland China |       81589 |     3318 |       76408 |     1863 |      4.06672 |       93.6499   |
| France         |       59929 |     5398 |       12548 |    41983 |      9.00733 |       20.9381   |
| Iran           |       50468 |     3160 |       16711 |    30597 |      6.26139 |       33.1121   |
| UK             |       34173 |     2926 |         192 |    31055 |      8.56232 |        0.561847 |
| Switzerland    |       18827 |      536 |        4013 |    14278 |      2.84698 |       21.3151   |
| Turkey         |       18135 |      356 |         415 |    17364 |      1.96305 |        2.28839  |


Rates are reported in percentage.

## Confirmed Cases for Top Countries

![Pie confirmed](images/eda/pie_confirmed.png "Pie confirmed")

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

### Time window = Last 15 days
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

### Germany Today
![Germany's doubling time](images/doubling_time/Germany.png "Germany's doubling time")
Growth for Germany considering the last 15 days.

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

## Germany
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




