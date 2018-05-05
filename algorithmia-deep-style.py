import Algorithmia

try:    
    with open('./secrets/algorithmia.key','r') as f:
        API_KEY = f.read()
except:
    print("You must create \"/secrets/algorithmia.key\" with your API key on it.")

filters = ["alien_goggles",
           "aqua",
           "blue_brush",
           "blue_granite",
           "bright_sand",
           "cinnamon_rolls",
           "clean_view",
           "colorful_blocks",
           "colorful_dream",
           "crafty_painting",
           "creativity",
           "crunch_paper",
           "dark_rain",
           "darK-soul",
           "deep_connections",
           "dry_skin",
           "far_away",
           "gan_vogh",
           "gred_mash",
           "green_zuma",
           "hot_spicy",
           "neo_instinct",
           "oily_mcoilface",
           "plentiful",
           "post_modern",
           "purp_paper",
           "purple_pond",
           "rainbow_festival",
           "really_hot",
           "sand_paper",
           "smooth_ride",
           "space_pizza",
           "spagetti_accident",
           "sunday",
           "yellow_collage",
           "yellow_paper"]



input = {"images": ["data://simon_bdz/huskies/10.jpg"], 
        "savePaths": ["data://simonbdz/stylized/10.jpg"], 
        "filterName": "space_pizza"}
client = Algorithmia.client(API_KEY)
algo = client.algo('deeplearning/DeepFilter/0.5.3')

print(algo.pipe(input))

