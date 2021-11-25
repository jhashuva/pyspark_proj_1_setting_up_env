from init_context import sp as spark,sc, app_name
if sc:
    print("Initalized Spark Context")

if spark:
    print("Initialized Spark Instance")

if app_name:
    print(f'App Name is {app_name}')
