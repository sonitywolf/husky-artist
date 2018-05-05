import Algorithmia

input = {"images": ["_IMAGE_URL_"], 
        "savePaths": ["_OUTPUT_URL_"], 
        "filterName": "space_pizza"}
client = Algorithmia.client('_API_KEY_')
algo = client.algo('deeplearning/DeepFilter/0.5.3')

print algo.pipe(input)