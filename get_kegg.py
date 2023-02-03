import requests

def get_metabolic_pathways(species_name):
    # Define the URL for the KEGG API request
    api_url = "https://rest.kegg.jp/list/pathway/{}".format(species_name)
    
    # Send the API request
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Split the response into separate lines
        lines = response.text.split("\n")
        
        # Extract the metabolic pathway information from the lines
        metabolic_pathways = [line.split("\t")[1] for line in lines if line]
        
        return metabolic_pathways
    else:
        return None

species_name = "Rhodococcus sp. ARC_M12"
pathways = get_metabolic_pathways(species_name)

if pathways:
    print("Metabolic pathways for {}:".format(species_name))
    for pathway in pathways:
        print(pathway)
else:
    print("No information found for species {}".format(species_name))
