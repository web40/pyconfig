import yaml

with open('settings.yaml',mode='w') as yamlFile:
  newSettings = {
    'database':
    {
      'user':'kofi',
      'server':'127.0.0.1',
      'password':'admin'
    }
  }

  newData = yaml.dump(newSettings,yamlFile)
  print(newData)



 