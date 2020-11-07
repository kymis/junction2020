import json


def parse_fundings():

    file = open('../Data/data.json')
    # dictionary
    data = json.load(file)

    final_data = []

    for e in data["haku"]:
        # basic details
        d = {
            "Funding_ID": e["id"],
            "Content_name": e["content"]["name"]["fi"],
            "Duration": e["content"]["duration"]["end"],
            "Self_financing_percentage": e["content"]["self-financing-percentage"],

        }

        if "rahoitusalueet" in e["content"] and len(e["content"]["rahoitusalueet"]) > 0:
            d["Funding_areas"] = e["content"]["rahoitusalueet"]

        if "total-grant-size" in e["content"]:
            d["Total_grant_size"] = e["content"]["total-grant-size"]

    final_json = json.dumps(final_data, indent=4)
    return final_json
