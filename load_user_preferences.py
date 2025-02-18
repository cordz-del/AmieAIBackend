def reimport():
  import sys
  import importlib

  # Remove the module from sys.modules
  module_name = 'ad_user_preferences'
  if module_name in sys.modules:
      del sys.modules[module_name]

  # Reimport the module
  importlib.import_module(module_name)
  print(f"Module {module_name} reimported successfully.")

