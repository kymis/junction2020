import json

kunnat = []


def create_city_list():
    file = open("Data/kunnat.csv")
    all_lines = file.readlines()
    for line in all_lines:
        city = line.split(",")[0]
        kunnat.append(city)


# fill the list
create_city_list()


# longest common substring
def LCSubStr(X, Y, m, n):
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    result = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result


# NEURAL NETWORK
def find_city(organization_name):
    l = len(organization_name)

    for city in kunnat:
        n = len(city)
        or_name_len = len(organization_name.split(" ")[0])
        print(or_name_len)
        if (n + 3) > or_name_len:
            longest_sub = LCSubStr(organization_name.split(" ")[0], city, l, n)
            if longest_sub >= n - 1:
                return city


def parse_projects():
    file = open('../Data/data.json')

    # dictionary
    data = json.load(file)

    final_data = []

    for e in data["loppuselvitys"]:
        # basic details
        d = {
            "Project_ID": e["haku_id"],
            "Project_name": e["project_name"],
            "Organization_name": e["organization_name"]
        }
        # find the city for the organization
        city = find_city(e["organization_name"])
        if city:
            d["City"] = city
        else:
            d["City"] = "-"

        v = e["loppuselvitys_answers"]["value"]
        for obj in v:
            # costs
            if obj["key"] == "personnel-costs-row.amount":
                d["personnel-costs"] = obj["value"]
            elif obj["key"] == "other-costs-row.amount":
                d["other-costs"] = obj["value"]
            elif obj["key"] == "steamship-costs-row.amount":
                d["steamship-costs"] = obj["value"]
            elif obj["key"] == "equipment-costs-row.amount":
                d["equipment-costs"] = obj["value"]
            elif obj["key"] == "material-costs-row.amount":
                d["material-costs"] = obj["value"]
            elif obj["key"] == "coordination-costs-row.amount":
                d["coordination-costs"] = obj["value"]
            elif obj["key"] == "rent-costs-row.amount":
                d["rent-costs"] = obj["value"]
            elif obj["key"] == "service-purchase-costs-row.amount":
                d["service-purchase-costs"] = obj["value"]
            elif obj["key"] == "project-description":
                d["project-goal"] = obj["value"][0]["value"][0]["value"]

                # incomes
            if obj["key"] == "project-incomes-row.amount":
                d["project-incomes"] = obj["value"]
            elif obj["key"] == "other-public-financing-income-row.amount":
                d["other-public-financing-income"] = obj["value"]
            elif obj["key"] == "private-financing-income-row.amount":
                d["private-financing-income"] = obj["value"]
            elif obj["key"] == "eu-programs-income-row.amount":
                d["eu-programs-income"] = obj["value"]

            # outcomes
            elif obj["key"] == "project-outcomes":
                outcome_values = obj["value"][0]["value"]
                for dv in outcome_values:
                    if dv["key"] == "project-outcomes.project-outcomes-1.outcome-type":
                        d["Project_outcomeType"] = dv["value"]
                    elif dv["key"] == "project-outcomes.project-outcomes-1.description":
                        d["Project_outcome"] = dv["value"]
        print(d)
        final_data.append(d)

    final_json = json.dumps(final_data, indent=4)
    return final_json


data = parse_projects()
