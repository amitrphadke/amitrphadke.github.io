import json
from pydantic import BaseModel, ValidationError
from common import MODEL, client

class Person(BaseModel):
    name: str
    age: int
    city: str

def via_instruction(text: str, retries: int = 1) -> Person:
    # TODO: system="Reply with JSON only: {name, age, city}" ; loop: parse+validate; on failure retry with the error message appended
    raise NotImplementedError

def via_tool(text: str) -> Person:
    tool = {"name": "record_person", "description": "Record the person described in the text.",
            "input_schema": Person.model_json_schema()}
    # TODO: call with tools=[tool], tool_choice={"type":"tool","name":"record_person"}; find the tool_use block; Person(**block.input)
    raise NotImplementedError

def extract_person(text: str) -> Person:
    return via_tool(text)

if __name__ == "__main__":
    print(extract_person("Amit, 44, lives in Pune and builds DevOps pipelines."))
