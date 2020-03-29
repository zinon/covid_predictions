<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics

- Last update: 2020-03-28 00:00:00
- Total confirmed cases: 660706
- Total death cases: 30651
- Total active cases: 492178
- Total recovered cases: 137877
- Death rate %: 4.64

 | Country        |   Confirmed |   Deaths |   Recovered |   Active |   Death Rate |   Recovery Rate |
|:---------------|------------:|---------:|------------:|---------:|-------------:|----------------:|
| US             |      121478 |     2026 |           0 |   119452 |     1.66779  |        0        |
| Italy          |       92472 |    10023 |       12384 |    70065 |    10.839    |       13.3922   |
| Mainland China |       81401 |     3295 |       74978 |     3128 |     4.04786  |       92.1094   |
| Spain          |       73235 |     5982 |       12285 |    54968 |     8.16823  |       16.7748   |
| Germany        |       57695 |      433 |        8481 |    48781 |     0.750498 |       14.6997   |
| France         |       38105 |     2317 |        5724 |    30064 |     6.08057  |       15.0217   |
| Iran           |       35408 |     2517 |       11679 |    21212 |     7.10856  |       32.9841   |
| UK             |       17312 |     1021 |         151 |    16140 |     5.89764  |        0.872227 |
| Switzerland    |       14076 |      264 |        1530 |    12282 |     1.87553  |       10.8696   |
| Netherlands    |        9819 |      640 |           6 |     9173 |     6.51798  |        0.061106 |


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
<img src="https://render.githubusercontent.com/render/math?math=y(t) = g(t) + s(t) + h(t) + \epsilon_\text{t}">
where
<img src="https://render.githubusercontent.com/render/math?math=g(t)">
represents the trend,
<img src="https://latex.codecogs.com/svg.latex?\Large&space;s(t)" />
the periodic component,
<img src="https://latex.codecogs.com/svg.latex?\Large&space;h(t)" />
holiday related events and
<img src="https://latex.codecogs.com/svg.latex?\Large&space;\epsilon_\text{t}" />
the error. The data are provided on a daily basis.
Also, the current model is not aware of holidays.

## Predictions for global confirmed cases.

### Linear model
![linear confrimed](images/predictions/prophet_linear_confirmed_prediction.png)

### Logistic model
![](images/predictions/prophet_logistic_confirmed_prediction.png)

## Predictions for global death cases.

### Linear model
![](images/predictions/)

### Logistic model
![](images/predictions/)

## Predictions for global active cases.

### Linear model
![](images/predictions/)

### Logistic model
![](images/predictions/)

## Predictions for global recovered cases.

### Linear model
![](images/predictions/)

### Logistic model
![](images/predictions/)





### Predictions for total confirmed cases using a logistic model.
![](images/predictions/)

### Predictions for total confirmed cases using a logistic model.
![](images/predictions/)
![](images/predictions/)
![](images/predictions/)
![](images/predictions/)



![Prophet Linear](images/predictions/prophet_linear_confirmed.png)
Predictions for total confirmed cases using a linear model.

![Prophet Linear Components](images/prophet_linear_confirmed_components.png "Components")
Components of linear forecasting model.

![Prophet Logistic](images/prophet_logistic_confirmed.png "Predictions")
Predictions for total confirmed cases using a logistic model.

![Prophet Logistic Components](images/prophet_logistic_confirmed_components.png "Components")
Components of logistic forecasting model.

![Prophet mortality](images/prophet_mortality.png "Predictions mortality rate")
Predictions for mortality rate.

![Prophet deaths](images/prophet_deaths.png "Predictions deaths")
Predictions for deaths using a logistic model.
