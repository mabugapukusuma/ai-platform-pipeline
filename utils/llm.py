import json

def call_llm(prompt: str):
    prompt_lower = prompt.lower().strip()

    # 🔹 Normalize vague inputs
    if len(prompt_lower.split()) <= 2:
        prompt_lower += " generic application"

    # 🔹 Keyword groups (stronger detection)
    app_map = {
        "E-commerce": ["ecommerce", "e-commerce", "shopping", "store", "marketplace", "cart", "checkout", "product"],
        "Chat App": ["chat", "messaging", "message", "conversation"],
        "Social Media": ["social", "posts", "likes", "comments", "followers"],
        "Blog Platform": ["blog", "article", "post", "content"],
        "Hospital Management": ["hospital", "patient", "doctor", "appointment", "medical"],
        "School Management": ["school", "education", "student", "attendance", "grades"],
        "Banking System": ["bank", "transaction", "account", "balance", "payment"],
        "Food Delivery": ["food", "restaurant", "menu", "order", "delivery"],
        "Ride Booking": ["ride", "taxi", "driver", "booking", "cab"],
        "Job Portal": ["job", "career", "hiring", "resume", "apply"]
    }

    # 🔹 Detect app type
    app_type = "Generic App"
    features = ["basic functionality", "user interface"]

    for app, keywords in app_map.items():
        if any(word in prompt_lower for word in keywords):
            app_type = app

            # 🔹 Assign features dynamically
            feature_map = {
                "E-commerce": ["login", "product listing", "cart", "checkout"],
                "Chat App": ["login", "messaging", "notifications"],
                "Social Media": ["login", "posts", "likes", "comments"],
                "Blog Platform": ["login", "create post", "edit post"],
                "Hospital Management": ["patient records", "appointments"],
                "School Management": ["student records", "attendance"],
                "Banking System": ["transactions", "balance check"],
                "Food Delivery": ["menu", "order", "tracking"],
                "Ride Booking": ["booking", "driver tracking"],
                "Job Portal": ["job listing", "apply"]
            }

            features = feature_map.get(app, features)
            break

    # 🔹 Clean DB name
    safe_name = app_type.replace(" ", "").replace("-", "")

    # 🔹 Intent Stage
    if "extract structured intent" in prompt_lower:
        return json.dumps({
            "app_type": app_type,
            "features": features
        })

    # 🔹 Design Stage
    elif "system design" in prompt_lower:
        return json.dumps({
            "entities": ["User", f"{safe_name}Data"],
            "roles": ["admin", "user"],
            "flows": ["login", "main flow", f"{app_type} operations"]
        })

    # 🔹 Schema Stage
    elif "schema" in prompt_lower:
        return json.dumps({
            "ui": {
                "pages": ["Home", "Dashboard"],
                "components": ["Form", "Table"]
            },
            "api": {
                "endpoints": ["/login", "/getData", "/createData"]
            },
            "database": {
                "tables": ["Users", f"{safe_name}_Data"]
            },
            "auth": {
                "roles": ["admin", "user"],
                "permissions": ["read", "write"]
            }
        })

    # 🔹 Repair Stage
    elif "fix" in prompt_lower or "invalid" in prompt_lower:
        return json.dumps({
            "ui": {"pages": [], "components": []},
            "api": {"endpoints": []},
            "database": {"tables": []},
            "auth": {"roles": [], "permissions": []}
        })

    # 🔹 Default fallback (never crash)
    return json.dumps({
        "ui": {},
        "api": {},
        "database": {},
        "auth": {}
    })