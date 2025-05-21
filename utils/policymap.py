import yaml
from datahub.live_data_router import get_live_value

def load_policy(filepath="datahub/live_policy.yaml"):
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def check_policy_effects():
    policy = load_policy()
    activated = {
        "sim": [],
        "zielprofil": {},
        "hinweise": []
    }

    for key, config in policy.items():
        current = get_live_value(key)
        if current is not None and current > config.get("warnwert", float("inf")):
            for effect_key, effect in config["effekte"].items():
                if effect_key.startswith("zielprofil."):
                    ziel = effect_key.split(".")[1]
                    delta = int(effect.replace("+", "")) if "+" in effect else int(effect)
                    activated["zielprofil"].setdefault(ziel, 0)
                    activated["zielprofil"][ziel] += delta
                elif effect_key.startswith("sim"):
                    activated["sim"].append(effect_key)
                    activated["hinweise"].append(effect)
    return activated
