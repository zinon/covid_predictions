# COVID-19 Predictions

## Data Source
https://github.com/CSSEGISandData/COVID-19

## Overall Statistics

- Last update: 2020-03-26 00:00:00
- Total confirmed cases: 529591
- Total death cases: 23969
- Total recovered cases: 121285
- Death rate %: 4.53

 | Country        |   Confirmed |   Deaths |   Recovered |   Death Rate |   Recovery Rate |   Active |
|:---------------|------------:|---------:|------------:|-------------:|----------------:|---------:|
| US             |       83836 |     1209 |           0 |     1.4421   |         0       |    82627 |
| Mainland China |       81298 |     3287 |       74061 |     4.04315  |        91.0982  |     3950 |
| Italy          |       80589 |     8215 |       10361 |    10.1937   |        12.8566  |    62013 |
| Spain          |       57786 |     4365 |        7015 |     7.55373  |        12.1396  |    46406 |
| Germany        |       43938 |      267 |        5673 |     0.607674 |        12.9114  |    37998 |
| France         |       29551 |     1698 |        4955 |     5.746    |        16.7676  |    22898 |
| Iran           |       29406 |     2234 |       10457 |     7.59709  |        35.5608  |    16715 |
| UK             |       11812 |      580 |         150 |     4.91026  |         1.2699  |    11082 |
| Switzerland    |       11811 |      191 |         131 |     1.61714  |         1.10914 |    11489 |
| South Korea    |        9241 |      131 |        4144 |     1.4176   |        44.8436  |     4966 |


## Overview 
![Overview stats](images/overview.png?raw=true "Overview")
Overview statistics for top affected countries.

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
