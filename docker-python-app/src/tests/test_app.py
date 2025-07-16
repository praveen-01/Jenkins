from app import app

def test_within_limit():
    client = app.test_client()
    for i in range(5):
        response = client.get("/app/route")
    return response.status_code == 200

def test_outside_limit():
    client = app.test_client()
    for i in range(7):
        response = client.get("/app/route")
    return response.status_code == 429
