def test_sign_up(client):
    r = client.post("/auth/signup", data={"username": "test", "password": "1234"})

    assert r.status_code == 201


def test_login(client, add_user):
    password = "1234"
    user = add_user(password=password)

    r = client.post("/auth/login", data={"username": user.username, "password": password})

    assert r.status_code == 200


def test_get_current_user(client, add_user):
    password = "1234"
    user = add_user(password=password)

    r = client.post("/auth/login", data={"username": user.username, "password": password})
    access_token = r.json()["access_token"]

    r = client.get("/auth/me", headers={"Authorization": f"Bearer {access_token}"})

    assert r.status_code == 200
    assert r.json()["id"] == user.id
