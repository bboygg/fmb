# FMB Backend 

## How to Start 
```python
# Activate venv
$source venv/bin/activate  

# Deactivate venv
$deactivate
# Start Server with reload
$uvicorn app.main:app --reload

# Reload server when only main.py changed 
$uvicorn app.main:app --reload-dir main.py
```


Study: 
https://medium.com/@iambkpl/setup-fastapi-and-sqlalchemy-mysql-986419dbffeb

https://www.youtube.com/watch?v=zzOwU41UjTM&list=PLpnKtSvDjVadWDdutt1ZeNGozDczQfZeo&index=7

https://github.com/CodeSeoul/complete-fastapi-example/blob/main/src/app/schemas.py

https://github.com/tiangolo/full-stack-fastapi-template/tree/master/backend

