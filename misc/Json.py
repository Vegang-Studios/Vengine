import json

with open('game.json') as file:
    data = json.load(file)

def getProjectName():
    for projectName in data['main']:
        return projectName['projectName']
    
def getPublicName():
    for publicName in data['main']:
        return publicName['publicName']

def getGameTitle():
    for title in data['gameInfos']:
        return title['title']
    
def getGameVersion():
    for version in data['gameInfos']:
        return version['version']
    
def getEngineVersion():
    for version in data['engineInfos']:
        return version['version']
    
def getStableVersion():
    for version in data['engineInfos']:
        return version['stableVersion']
    
if getStableVersion() == False:
    print("Version non stable, il peut y avoir des bugs.")