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
