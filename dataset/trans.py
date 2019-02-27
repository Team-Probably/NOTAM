import json
import csv
from googletrans import Translator

message_prior = []
with open('raw.json') as json_lines:
    for json_line in json_lines:
        data = json.loads(json_line)
        message_prior.append([data["message"], data["criticality"]])


def trans(inp):
    translator = Translator()
    res = translator.translate(inp)
    return res.text


lineno = []
print("start")
with open('train2.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(["Message", "Criticality"])
    for line in message_prior:
        og_line = line[0]
        try:
            line[0] = trans(og_line)
        except:
            continue
        print(og_line, line[0])
        count += 1
        lineno.append(line)
        writer.writerow(line)

print(lineno)
