# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics
- Last update: 2020-05-05 00:00:00
- Total confirmed cases: 3662691
- Total death cases: 257239
- Total active cases: 2423417
- Total recovered cases: 982035
- Death rate %: 7.02

 | Country   |        Confirmed |   Deaths |   Recovered |           Active |   Death Rate |   Recovery Rate |
|:----------|-----------------:|---------:|------------:|-----------------:|-------------:|----------------:|
| US        |      1.20435e+06 |    71064 |           0 |      1.13329e+06 |      5.90061 |        0        |
| Spain     | 219329           |    25613 |      123486 |  70230           |     11.6779  |       56.3017   |
| Italy     | 213013           |    29315 |       85231 |  98467           |     13.7621  |       40.0121   |
| UK        | 196243           |    29501 |         926 | 165816           |     15.0329  |        0.471864 |
| France    | 170687           |    25537 |       52842 |  92308           |     14.9613  |       30.9584   |
| Germany   | 167007           |     6993 |      135100 |  24914           |      4.18725 |       80.8948   |
| Russia    | 155370           |     1451 |       19865 | 134054           |      0.9339  |       12.7856   |
| Turkey    | 129491           |     3520 |       73285 |  52686           |      2.71834 |       56.5947   |
| Brazil    | 115455           |     7938 |       48221 |  59296           |      6.87541 |       41.7661   |
| Iran      |  99970           |     6340 |       80475 |  13155           |      6.3419  |       80.4991   |

Rates are reported in percentage.

## Demystification of the Death Rates reported by Mass Media

Re-evaluated Death Rate
- Consider the smallest x-fold lower risk of COVID-19 death: 36
- Re-evaluated death rate: 0.20%

This is "as equivalent of death risk from driving a motor vehicle" according to  [Population-level COVID-19 mortality risk for non-elderly individuals overall and for non-elderly individuals without underlying diseases in pandemic epicenters, J. P. A. Ioannidis et al. (Stanford University School of Medicine)](https://www.medrxiv.org/content/10.1101/2020.04.05.20054361v2).


According to the [Ministero della Salute](http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=italiano&id=5351&area=nuovoCoronavirus&menu=vuoto) of Italy
- Conisder that only 3.80% of the deaths had previously NO pathologies 
- The re-evaluated death rate for Italy becomes 0.52%

which turns to be at the level of a seasonal influenza (for which additionally vaccination is available).

Many studies reveal that seasonal influenza has more severe burdens. See for example, the study in this article [Global mortality associated with seasonal influenza epidemics: ...](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6815659/) where it is stated that "an average of 389 000 (uncertainty range 294 000-518 000) respiratory deaths were associated with influenza globally 
each year during the study period, corresponding to ~2% of all annual respiratory deaths".

For other diseases, such as whooping cough, despite they are much more dangerous, no draconian measures or lockdowns are taken. For example,
Pertussis, caused by Bordetella pertussis and for which there's vaccination, is endemic in all countries. Globally, it is estimated that there were 24.1 million pertussis cases and 160 700 deaths from pertussis in children < 5 years of age in 2014, according to this [reference](https://www.who.int/immunization/monitoring_surveillance/burden/vpd/WHO_SurveillanceVaccinePreventable_16_Pertussis_R1.pdf?ua=1).


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

![Mortality rate per minute](images/eda/daily_death_rate_global.png?raw=true "Mortality rate / minute")
Mortality per minute worldwide.

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

### Time window - Last 25 days (06.05.2020)
|    | Country   |   Doubling Time |   Doubling Time Error |
|---:|:----------|----------------:|----------------------:|
|  3 | Spain     |        197.108  |            132.198    |
|  4 | France    |        118.915  |             10.5378   |
|  5 | Greece    |         84.4565 |              9.47842  |
|  0 | Germany   |         82.55   |              4.10417  |
|  2 | Italy     |         65.5015 |              2.58676  |
|  6 | US        |         24.6406 |              0.571902 |
|  1 | UK        |         23.5213 |              0.392355 |


### Time window - Last 25 days (19.04.2020)
|    | Country   |   Doubling Time |   Doubling Time Error |
|---:|:----------|----------------:|----------------------:|
|  5 | Greece    |         50.5614 |              3.30644  |
|  0 | Germany   |         42.3396 |              1.32327  |
|  4 | France    |         41.145  |              3.49685  |
|  2 | Italy     |         38.5042 |              0.946665 |
|  3 | Spain     |         30.4402 |              0.64704  |
|  6 | US        |         17.0534 |              0.356988 |
|  1 | UK        |         15.7245 |              0.440931 |

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

* Growth Factor
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
 <img src="https://render.githubusercontent.com/render/math?math=\ln(2)" />
to the constant
 <img src="https://render.githubusercontent.com/render/math?math=k" />.

### Growth factor
![GF](images/factor_analysis/growth_factor_Germany.png)

The growth factor on day D is the number of confirmed cases on day D minus confirmed cases on day D-1 divided by the number of confirmed cases on day D-1 minus confirmed cases on day D-2:

<img src="https://render.githubusercontent.com/render/math?math=\tfrac{N_i - N_{i-1}}{N_{i-1}-N_{i-2}}" />

with

<img src="https://render.githubusercontent.com/render/math?math=i" /> = days, weeks, months, years, ...

### Growth ratio
![GRat](images/factor_analysis/growth_ratio_Germany.png)

The growth ratio on day D is the number of confirmed cases on day D divided by the number of confirmed cases on day D-1:

<img src="https://render.githubusercontent.com/render/math?math=\tfrac{N_i}{N_{i-1}}" />.

### Second derivative of exponential growth
![2ndDer](images/factor_analysis/second_derivative_Germany.png)
