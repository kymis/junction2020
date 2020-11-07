import json
import funding_parser as fp
import project_parser as pp

projects_json = pp.parse_projects()

print(projects_json)

with open("Processed_data/projects.json", "w") as outfile:
    outfile.write(projects_json)
