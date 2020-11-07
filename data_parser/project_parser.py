import json

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
        elif obj["key"] == "coodination-costs-row.amount":
            d["coordination-costs"] = obj["value"]
        elif obj["key"] == "rent-costs-row.amount":
            d["rent-costs"] = obj["value"]
        elif obj["key"] == "service-purchase-costs-row.amount":
            d["service-purchase-costs"] = obj["value"]

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
    with open("../Processed_data/projects.json", "w") as outfile:
        outfile.write(final_json)

