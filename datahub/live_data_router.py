import yaml

def get_live_value(path, base_path="datahub/valori_livedata.yaml"):
    with open(base_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    for part in path.split("."):
        data = data.get(part, {})
    return data if isinstance(data, (int, float, str)) else None
