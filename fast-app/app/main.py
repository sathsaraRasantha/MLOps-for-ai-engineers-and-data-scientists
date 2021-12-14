from fastapi import FastAPI, Request
from area import area_in_acres

# instantiate fastapi
app = FastAPI()


@app.get("/")
async def get_input(request:Request):
    """
        Get inputs from users and call the simple interest function to evaluate
        the parameters then return the output.
    """
    getInput = await request.json()
    length = getInput['length']
    width = getInput['width']

    # evaluate interest
    area = area_in_acres(length,width)

    return {"area in acres":area}


