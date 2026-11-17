#good example of how to parse json so i dont have to look for things like an animal 
# expected output: Thu, November 12th at 8:15 PM EST

import json
data = json.load(open("tests/fixtures/nfl_one_game.json"))
comp = data["events"][0]["competitions"][0]
print(comp["status"]["type"]["detail"])