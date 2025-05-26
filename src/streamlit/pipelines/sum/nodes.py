"""
This is a boilerplate pipeline 'sum'
generated using Kedro 0.19.12
"""
#def compute_sum(numbers: list) -> dict:
    #return {"sum": sum(numbers)}

def compute_sum(data: dict) -> dict:
    numbers = data["numbers"]
    return {"sum": sum(numbers)}


