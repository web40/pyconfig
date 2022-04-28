import yaml

with open('settings.yaml',mode='r') as yamlFile:
  print(yaml.safe_load(yamlFile))