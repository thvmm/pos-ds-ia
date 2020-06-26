import pandas as pd
from itertools import product
import names
import random
import uuid
from datetime import datetime, timedelta
from sqlalchemy import create_engine


def create_villain_data(N=100):
    result = {}
    superVillains = ["The Lazy Lion","The Hungry Scorpion","The Gigantic Waspman","The Voiceless Mage","Absent Monarch","Awful Sage","Upset Creature","Agent Blue Masquerade","The Reaper","Silverclaw","The Unwritten Puma","The Real Falcon","The Gigantic Nighthawk","The Thin Slayer","Curious Mercenary","Agent Puzzling Master","Captain Third Marksman","Captain Blue Fox","Tecton","Miss Guidance","The Pink Demon","The Handy Mongoose","The Awful Magician","The Hungry Swordsman","Master Mute Freak","Proud Wolfman","Cowardly Mongoose","Master Misty Mole","Eva Destruction","Catastrophe","The Ice Scimitar","The Dramatic Zombie","The Talented Gorilla","The Repulsive Gloom","Absent Raven","Ice Scout","Shaggy Siren","Professor Fiery Slayer","Brain Freeze","Meltdown","The Aggressive Burglar","The Limping Wonder","The Adorable Devil","The Unusual Starling","Master Earthen Marksman","Captain Smooth Cricket","Professor Special Crane","Defiant Wonderman","Disembowler","Bronze Butcher","The Thin Beetle","The Electric Antman","The Deranged Mastermind","The Light Mantis","Lord Ugly Whiz","Unnatural Android","Professor Electron Wonder","Fiery Knuckles","Tasmanian Tiger","Miss Judgement","The Blue Hijacker","The Rare Assassin","The Mute Cricket","The Dazzling Beetle","Master Ghost Sage","Nimble Enchanter","Commander Rapid Bandit","Dynamic Starling","Faye Tality","Catastrophe","The Last Conjurer","The Wretched Gangster","The Ruthless Merlin","The Hypnotic Angel","Gullible Jackal","Water Genius","Secret Nightowl","Agent Frightening Mugger","The Black Falcon","Disembowler","The Huge Assassin","The Messy Hawk","The Wise Doctor","The Greasy Shadow","Master Creepy Clown","Frightening Duke","Agent Flashy Scorpion","Puzzling Beetle","Arachnis","he Spooky Prophet","The Colossal Horror","The Wild Wolverine","The Second Eagle","Gifted Dragonfly","Talented Mugger","Mister Second Scepter","Yellow Ant","Miss Judgement","Warped Warrior","The Rabid Whiz","The Light Agent","The Proud Master","The Lonely Arsonist","Master Copper Shadow","Agent Molten Mercenary","Doctor Electric Scout","Nimble Haunt","Black Cat","Miss Chievous"]
    weaknesses_list = ['Kryptonite', 'Acidic Substances', 'Arrogance', 'Recklessness', 'Obesity', 'Anorexia', 'Clumsiness', 'you are a Crybaby', 'Depression', 'that you have a Low Self-Esteem', 'you are Easily Manipulated', 'Lactose Intolerance', 'Diabetes']
    nomeFantasia = pd.Series(superVillains).sample(N)
    realNames = [names.get_full_name() for x in range(N)]
    weaknesses = [", ".join(random.choices(weaknesses_list, k=random.randint(0,10))) for x in range(N)]
    batID = [str(uuid.uuid4()) for x in range(N)]
    idades = [random.randint(15,200) for x in range(N)]
    result = {
        "BatID" : batID,
        "NomeFantasia" : nomeFantasia,
        "NomeReal" : realNames,
        "Idade" : idades,
        "Fraqueza" : weaknesses
    }
    return pd.DataFrame(result)

def create_super_hero_data(N=100):
    fFantasyName = ['Wonder ', 'Super ', 'X ', 'King','Queen ', 'Tornado ', 'Cyclone ', 'Atomic ', 'Demon ', 'Draconis ', 'Lord', 'Lady ', 'One Punch ', 'Beast-', 'Eternal ', 'Ultimate ', 'Justice ', 'Laser ', 'Demon ', 'Superior ', 'Iron ', 'Crystal ', 'Fat ', 'Blast ', '', 'The Amazing ', 'Indominus ']
    sFantasyname = ['Boy','Girl', 'Man', 'Woman', 'Black Hole', 'Master', 'Sensei', 'Genesect', 'Samuri', 'Ninja', 'Saiyan', 'Knight', 'Guardian', 'Protector', 'Terror', 'Emperor', 'Diamond', 'Angel', 'Hunter', 'Rocket', 'Dynamite', 'Cyborg', 'Sorceror', '', 'Swordsman', 'God']
    superpowers_list = ['Flight', 'X-Ray Vision', 'Laser Eyes', 'Super Strength', 'Super Speed', 'Regeneration', 'Telekinesis', 'Hypnosis', 'Martial Arts Mastery', 'Incredible Combat Skill', 'Magical Abilities', 'Incredible Genius', 'insane Swordskills']
    weaknesses_list = ['Kryptonite', 'Acidic Substances', 'Arrogance', 'Recklessness', 'Obesity', 'Anorexia', 'Clumsiness', 'you are a Crybaby', 'Depression', 'that you have a Low Self-Esteem', 'you are Easily Manipulated', 'Lactose Intolerance', 'Diabetes']
    nomeFantasia = pd.Series([*product(fFantasyName,sFantasyname)]).apply(lambda x: " ".join(x)).sample(N)
    realNames = [names.get_full_name() for x in range(N)]
    weaknesses = [", ".join(random.choices(weaknesses_list, k=random.randint(0,10))) for x in range(N)]
    superpower = [", ".join(random.choices(superpowers_list, k=random.randint(0,3))) for x in range(N)]
    batID = [str(uuid.uuid4()) for x in range(N)]
    result = {
        "BatID" : batID,
        "NomeFantasia" : nomeFantasia,
        "NomeReal" : realNames,
        "Poder" : superpower
    }
    return pd.DataFrame(result)

def create_arquiinimigo_data(super_hero_df, villain_df):
    result = {
        "BatIDHeroi" : super_hero_df["BatID"],
        "BatIDVilao" : [ villain_df["BatID"].sample(1).iloc[0] for x in range(super_hero_df.shape[0])]
    }
    return pd.DataFrame(result)

def create_localizacao_data(N=100):
    places_list = ["West Kilboolyass", "Saint Cryla", "Romcrymouth", "Kemlowsda", "Ldenrelworthnorth", "Clispo Under Newsmi Point", "West Lens", "Yorvengaicombe", "Bramp", "Saint Wenwy", "West Lackan", "Damfallsniumtree", "Bridrentad", "Liotprice Aux Rusradington", "North Maxledge", "Park Molshe", "Teltham Du Memwill", "West Princehex", "Welchcowes", "Great Praislandwot", "San Tor", "Havstretsques Wells", "La Cusval", "Milin", "La Orbrook", "Santa Wkesficdruth", "Saint Telscruces", "Redting Forest", "Xemo With Fortsaintpool", "Rolksham Heath", "Nierstone Upon Skeardver-On-Sea", "East Tordiss", "Port Hingron", "Cape Ames", "West Oodup Aux Leskuuj", "Red Werhod", "Mount Marladfo", "Sconeglobe", "Fort Ledbeecken", "Fort Castbairns", "Dsportkenia", "Santa Plainslisgrays", "Cape Rierich", "Fort Chinemay", "New Tainwinsas", "Springspass", "Nchelsu Bend", "Chasecarsou Lake", "Port Unsenbou", "Viewking Aux Stiankmul Bay", "Ncouvecleworth", "Derryn", "Cetry", "Hentrailsham", "Nantstow Castle", "West Lyneners", "Heathfrithgate", "Moose Mathqa", "New Hawkwent", "Dunclun", "Katoto", "Cape Harde With Ventrsip", "Rntwoodwadrim Park", "Grand Monddiacre", "Towsealeighcombe", "Decklydchester", "Hillneckworth", "Stonepryorde", "Cape Sunken", "Port Nacce Aux Kiawing", "Moose Aucknton", "Locksaldsorgates", "Lake Whaswor", "Whittzion", "Port Miemer", "Thtonferdel Town", "Grand Tinix", "Stonmal Under Prestown Colonies", "North Centrebuc", "Bertham", "Grandhall Island", "Fort Vicdrew", "El Gracetroquences", "Saywler Bay", "Gussal Aux Ralpe", "Saint Xbuurnage", "Brotewye", "Port Cliffemor", "Chwoodbraun", "Tomdseyfax", "Royal Nel", "Terlick Springs", "Las Sanhuu", "Headchi", "Faifea", "Townboncinechester", "Netteflondon", "Kirkster", "Fernorthfolk Springs", "New Noawaurstone"]
    lats = [random.random() * 180 - 90 for x in range(len((places_list)))]
    longs = [random.random() * 360 - 180 for x in range(len((places_list)))]
    ids = [x for x in range(len(places_list))]
    result = {
        "lid" : ids,
        "PR" : ["West Kilboolyass", "Saint Cryla", "Romcrymouth", "Kemlowsda", "Ldenrelworthnorth", "Clispo Under Newsmi Point", "West Lens", "Yorvengaicombe", "Bramp", "Saint Wenwy", "West Lackan", "Damfallsniumtree", "Bridrentad", "Liotprice Aux Rusradington", "North Maxledge", "Park Molshe", "Teltham Du Memwill", "West Princehex", "Welchcowes", "Great Praislandwot", "San Tor", "Havstretsques Wells", "La Cusval", "Milin", "La Orbrook", "Santa Wkesficdruth", "Saint Telscruces", "Redting Forest", "Xemo With Fortsaintpool", "Rolksham Heath", "Nierstone Upon Skeardver-On-Sea", "East Tordiss", "Port Hingron", "Cape Ames", "West Oodup Aux Leskuuj", "Red Werhod", "Mount Marladfo", "Sconeglobe", "Fort Ledbeecken", "Fort Castbairns", "Dsportkenia", "Santa Plainslisgrays", "Cape Rierich", "Fort Chinemay", "New Tainwinsas", "Springspass", "Nchelsu Bend", "Chasecarsou Lake", "Port Unsenbou", "Viewking Aux Stiankmul Bay", "Ncouvecleworth", "Derryn", "Cetry", "Hentrailsham", "Nantstow Castle", "West Lyneners", "Heathfrithgate", "Moose Mathqa", "New Hawkwent", "Dunclun", "Katoto", "Cape Harde With Ventrsip", "Rntwoodwadrim Park", "Grand Monddiacre", "Towsealeighcombe", "Decklydchester", "Hillneckworth", "Stonepryorde", "Cape Sunken", "Port Nacce Aux Kiawing", "Moose Aucknton", "Locksaldsorgates", "Lake Whaswor", "Whittzion", "Port Miemer", "Thtonferdel Town", "Grand Tinix", "Stonmal Under Prestown Colonies", "North Centrebuc", "Bertham", "Grandhall Island", "Fort Vicdrew", "El Gracetroquences", "Saywler Bay", "Gussal Aux Ralpe", "Saint Xbuurnage", "Brotewye", "Port Cliffemor", "Chwoodbraun", "Tomdseyfax", "Royal Nel", "Terlick Springs", "Las Sanhuu", "Headchi", "Faifea", "Townboncinechester", "Netteflondon", "Kirkster", "Fernorthfolk Springs", "New Noawaurstone"],
        "lat" : lats,
        "long" : longs
    }
    return pd.DataFrame(result)

def create_localizacao_data(N=100):
    places_list = ["West Kilboolyass", "Saint Cryla", "Romcrymouth", "Kemlowsda", "Ldenrelworthnorth", "Clispo Under Newsmi Point", "West Lens", "Yorvengaicombe", "Bramp", "Saint Wenwy", "West Lackan", "Damfallsniumtree", "Bridrentad", "Liotprice Aux Rusradington", "North Maxledge", "Park Molshe", "Teltham Du Memwill", "West Princehex", "Welchcowes", "Great Praislandwot", "San Tor", "Havstretsques Wells", "La Cusval", "Milin", "La Orbrook", "Santa Wkesficdruth", "Saint Telscruces", "Redting Forest", "Xemo With Fortsaintpool", "Rolksham Heath", "Nierstone Upon Skeardver-On-Sea", "East Tordiss", "Port Hingron", "Cape Ames", "West Oodup Aux Leskuuj", "Red Werhod", "Mount Marladfo", "Sconeglobe", "Fort Ledbeecken", "Fort Castbairns", "Dsportkenia", "Santa Plainslisgrays", "Cape Rierich", "Fort Chinemay", "New Tainwinsas", "Springspass", "Nchelsu Bend", "Chasecarsou Lake", "Port Unsenbou", "Viewking Aux Stiankmul Bay", "Ncouvecleworth", "Derryn", "Cetry", "Hentrailsham", "Nantstow Castle", "West Lyneners", "Heathfrithgate", "Moose Mathqa", "New Hawkwent", "Dunclun", "Katoto", "Cape Harde With Ventrsip", "Rntwoodwadrim Park", "Grand Monddiacre", "Towsealeighcombe", "Decklydchester", "Hillneckworth", "Stonepryorde", "Cape Sunken", "Port Nacce Aux Kiawing", "Moose Aucknton", "Locksaldsorgates", "Lake Whaswor", "Whittzion", "Port Miemer", "Thtonferdel Town", "Grand Tinix", "Stonmal Under Prestown Colonies", "North Centrebuc", "Bertham", "Grandhall Island", "Fort Vicdrew", "El Gracetroquences", "Saywler Bay", "Gussal Aux Ralpe", "Saint Xbuurnage", "Brotewye", "Port Cliffemor", "Chwoodbraun", "Tomdseyfax", "Royal Nel", "Terlick Springs", "Las Sanhuu", "Headchi", "Faifea", "Townboncinechester", "Netteflondon", "Kirkster", "Fernorthfolk Springs", "New Noawaurstone"]
    lats = [random.random() * 180 - 90 for x in range(len((places_list)))]
    longs = [random.random() * 360 - 180 for x in range(len((places_list)))]
    ids = [x for x in range(len(places_list))]
    result = {
        "lid" : ids,
        "PR" : ["West Kilboolyass", "Saint Cryla", "Romcrymouth", "Kemlowsda", "Ldenrelworthnorth", "Clispo Under Newsmi Point", "West Lens", "Yorvengaicombe", "Bramp", "Saint Wenwy", "West Lackan", "Damfallsniumtree", "Bridrentad", "Liotprice Aux Rusradington", "North Maxledge", "Park Molshe", "Teltham Du Memwill", "West Princehex", "Welchcowes", "Great Praislandwot", "San Tor", "Havstretsques Wells", "La Cusval", "Milin", "La Orbrook", "Santa Wkesficdruth", "Saint Telscruces", "Redting Forest", "Xemo With Fortsaintpool", "Rolksham Heath", "Nierstone Upon Skeardver-On-Sea", "East Tordiss", "Port Hingron", "Cape Ames", "West Oodup Aux Leskuuj", "Red Werhod", "Mount Marladfo", "Sconeglobe", "Fort Ledbeecken", "Fort Castbairns", "Dsportkenia", "Santa Plainslisgrays", "Cape Rierich", "Fort Chinemay", "New Tainwinsas", "Springspass", "Nchelsu Bend", "Chasecarsou Lake", "Port Unsenbou", "Viewking Aux Stiankmul Bay", "Ncouvecleworth", "Derryn", "Cetry", "Hentrailsham", "Nantstow Castle", "West Lyneners", "Heathfrithgate", "Moose Mathqa", "New Hawkwent", "Dunclun", "Katoto", "Cape Harde With Ventrsip", "Rntwoodwadrim Park", "Grand Monddiacre", "Towsealeighcombe", "Decklydchester", "Hillneckworth", "Stonepryorde", "Cape Sunken", "Port Nacce Aux Kiawing", "Moose Aucknton", "Locksaldsorgates", "Lake Whaswor", "Whittzion", "Port Miemer", "Thtonferdel Town", "Grand Tinix", "Stonmal Under Prestown Colonies", "North Centrebuc", "Bertham", "Grandhall Island", "Fort Vicdrew", "El Gracetroquences", "Saywler Bay", "Gussal Aux Ralpe", "Saint Xbuurnage", "Brotewye", "Port Cliffemor", "Chwoodbraun", "Tomdseyfax", "Royal Nel", "Terlick Springs", "Las Sanhuu", "Headchi", "Faifea", "Townboncinechester", "Netteflondon", "Kirkster", "Fernorthfolk Springs", "New Noawaurstone"],
        "lat" : lats,
        "long" : longs
    }
    return pd.DataFrame(result) 

def create_avistou_data(super_hero_df,villain_df, localizacao_data, N=500):
    batHeroIds = [super_hero_df["BatID"].sample(1).iloc[0] for x in range(N) ]
    villainIds = [villain_df["BatID"].sample(1).iloc[0] for x in range(N) ]
    lids = [localizacao_data["lid"].sample(1).iloc[0] for x in range(N) ]
    avistou_ids = [x for x in range(N)]
    dates = [generate_datetime().strftime("%d/%m/%Y") for x in range(N)]
    result = {
        "avistouID" : avistou_ids,
        "lid" : lids,
        "BatIDHeroi" : batHeroIds,
        "BatIDVilao" : villainIds,
        "data" : dates
    }
    return pd.DataFrame(result)

def generate_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

if __name__ == "__main__":
    super_hero_df = create_super_hero_data()
    villain_df = create_villain_data()
    aquiinimigo_data = create_arquiinimigo_data(super_hero_df,villain_df)
    localizacao_data = create_localizacao_data()
    avistou_data = create_avistou_data(super_hero_df, villain_df, localizacao_data)

    # import ipdb;ipdb.set_trace()
    
    engine = create_engine('sqlite:///super_heroi.sqlite', echo=True)
    print("Adding super_hero")

    print(super_hero_df.to_sql('SuperHeroi', con=engine, if_exists='append', index=False))
    # print("Adding villain")
    # villain_df.to_sql('Vilao', con=engine, if_exists='append', index=False)
    # print("Adding Arquiinimigo")
    # aquiinimigo_data.to_sql('Arquiinimigo', con=engine, if_exists='append', index=False)
    # print("Adding Localizacao")
    # localizacao_data.to_sql('Localizacao', con=engine, if_exists='append', index=False)
    # print("Adding Avistou")
    # avistou_data.to_sql('Avistou', con=engine, if_exists='append', index=False)
