# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics

Overall statistics information
- Last update: 2020-03-23 00:00:00
- Total confirmed cases: 378287
- Total death cases: 16497
- Total recovered cases: 100958
- Death rate %: 4.36

| Country        |   Confirmed |   Deaths |   Recovered |   Death Rate |   Recovery Rate |   Active |
|:---------------|------------:|---------:|------------:|-------------:|----------------:|---------:|
| Mainland China |       81116 |     3270 |       72709 |      4.03126 |        89.6358  |     5137 |
| Italy          |       63927 |     6077 |        7432 |      9.50616 |        11.6258  |    50418 |
| US             |       43667 |      552 |           0 |      1.26411 |         0       |    43115 |
| Spain          |       35136 |     2311 |        3355 |      6.5773  |         9.54861 |    29470 |
| Germany        |       29056 |      123 |         453 |      0.42332 |         1.55906 |    28480 |
| Iran           |       23049 |     1812 |        8376 |      7.86151 |        36.34    |    12861 |
| France         |       20123 |      862 |        2207 |      4.28366 |        10.9675  |    17054 |
| South Korea    |        8961 |      111 |        3166 |      1.2387  |        35.3309  |     5684 |
| Switzerland    |        8795 |      120 |         131 |      1.36441 |         1.48948 |     8544 |
| UK             |        6726 |      336 |         140 |      4.99554 |         2.08147 |     6250 |


## Overall 
![Global growth](images/overall.png?raw=true "Global growth")
Overall statistics for top affected countries.

## Global growth
![Global growth](images/overall.png?raw=true "Global growth")
Global growth rate of confirmed cases.

## Leaders
![Leaders growth](images/leaders.png?raw=true "Leaders growth")
Confirmed cases for the most affected countries and Germany.

## Mortality
![Mortality rate](images/mortality.png?raw=true "Mortality rate")
Percentage mortality (death rate) for top affected countries and Germany.

## Percentage Rates
![Percentage Rates](images/rates.png?raw=true "Percentage rates")
Percentage rates for deaths, recovered cases and confirmed cases on a global scale. Mainland China is included.

# Predictions

## With Facebook Prophet

![Prophet Linear](images/prophet_linear_confirmed.png?raw=true "Predictions")
Predictions for total confirmed cases using a linear model.

![Prophet Linear Components](images/prophet_linear_confirmed_components.png?raw=true "Components")
Components of linear forecasting model.

![Prophet Logistic](images/prophet_logistic_confirmed.png?raw=true "Predictions")
Predictions for total confirmed cases using a logistic model.

![Prophet Logistic Components](images/prophet_logistic_confirmed_components.png?raw=true "Components")
Components of logistic forecasting model.

![Prophet mortality](images/prophet_mortality.png?raw=true "Predictions mortality rate")
Predictions for mortality rate.

![Prophet deaths](images/prophet_deaths.png?raw=true "Predictions deaths")
Predictions for deaths using a logistic model.
