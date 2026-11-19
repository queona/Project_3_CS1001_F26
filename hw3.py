import county_demographics
import data
import build_data

build_data.get_data()


# Part 1
def population_total(counties: list[data.CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population['2014 Population']
    return total


# Part 2
def filter_by_state(counties: list[data.CountyDemographics], state: str) -> list[data.CountyDemographics]:
    l = []
    for county in counties:
        if county.state == state:
            l.append(county)
    return l

# Part 3
def population_by_education(counties: list[data.CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        total += county.population['2014 Population'] * county.education[key] / 100
    return total
def population_by_ethnicity(counties: list[data.CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        total += county.population['2014 Population'] * county.ethnicities[key] / 100
    return total
def population_below_poverty_level(counties: list[data.CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        total += county.population['2014 Population'] * county.income[key] / 100
    return total

# Part 4
def percent_by_education(counties: list[data.CountyDemographics], key: str) -> float:
    return (100 * ((population_by_education(counties, key) / population_total(counties))))
def percent_by_ethnicity(counties: list[data.CountyDemographics], key: str) -> float:
    return (100 * ((population_by_ethnicity(counties, key) / population_total(counties))))
def percent_below_poverty_level(counties: list[data.CountyDemographics], key: str) -> float:
    return (100 * ((population_below_poverty_level(counties, key) / population_total(counties))))

# Part 5
def education_greater_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    l = []
    for county in counties:
        if county.education[key] > threshold:
            l.append(county)
    return l
def education_less_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    l = []
    for county in counties:
        if county.education[key] < threshold:
            l.append(county)
    return l
def ethnicity_greater_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    l = []
    for county in counties:
        if county.ethnicities[key] > threshold:
            l.append(county)
    return l
def ethnicity_less_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    l = []
    for county in counties:
        if county.ethnicities[key] < threshold:
            l.append(county)
    return l
def below_poverty_level_greater_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    l = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] > threshold:
            l.append(county)
    return l
def below_poverty_level_less_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    l = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] < threshold:
            l.append(county)
    return l