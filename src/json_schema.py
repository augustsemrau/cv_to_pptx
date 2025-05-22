import json
from jsonschema import Draft7Validator


def get_json_schema(return_string: bool = False):
    schema = {
        "type": "object",
        "required": ["name", "email", "phone", "title", "profile"],
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "phone": {"type": "string"},
            "title": {"type": "string"},
            "profile": {"type": "string"},
            "educations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["institution", "start_year", "end_year", "degree"],
                    "properties": {
                        "institution": {"type": "string"},
                        "start_year": {"type": "integer"},
                        "end_year": {"type": "integer"},
                        "degree": {"type": "string"}
                    }
                },
                "default": []
            },
            "skills": {"type": "array", "items": {"type": "string"}, "default": []},
            "certifications": {"type": "array", "items": {"type": "string"}, "default": []},
            "languages": {"type": "array", "items": {"type": "string"}, "default": []},
            "projects": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["name", "description"],
                    "properties": {
                        "name": {"type": "string"},
                        "description": {"type": "string"}
                    }
                },
                "default": []
            }
        },
        "additionalProperties": False
    }

    if return_string:
        return json.dumps(schema)
    return schema


def validate_json(data):
    schema = get_json_schema()
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        messages = []
        for error in errors:
            path = "/".join([str(p) for p in error.path]) or "root"
            messages.append(f"{path}: {error.message}")
        return False, "\n".join(messages)
    return True, ""
