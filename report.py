import json
import csv

def report_generator(search_results, json_flag):
    search_engine_json = search_results.get_json()

    header_csv_engine = ['Query', 'URL', 'Title', 'Description']
    header_csv_metadata = ['Engine', 'Query', 'Json endpoint', 'Search engine URL', 'Raw Html File']

    with open ("".join([search_engine_json["search_parameters"]["engine"], ".csv"]), "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(header_csv_engine)
        for fields in search_engine_json["organic_results"]:
            descriptor_list = []
            if "q" in search_engine_json["search_parameters"]:
                descriptor_list.append(search_engine_json["search_parameters"]["q"])
                descriptor_list.append(fields["link"])
                descriptor_list.append(fields["title"])
                descriptor_list.append(fields["snippet"])
                writer.writerow(descriptor_list)
            elif "text" in search_engine_json["search_parameters"]:
                descriptor_list.append(search_engine_json["search_parameters"]["text"])
                descriptor_list.append(fields["link"])
                descriptor_list.append(fields["title"])
                descriptor_list.append(fields["snippet"])
                writer.writerow(descriptor_list)
    
    with open("".join([search_engine_json["search_parameters"]["engine"], ".json"]), "w", encoding="utf-8") as file:
        json.dump(search_engine_json, file)