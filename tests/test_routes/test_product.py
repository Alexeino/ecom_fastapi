from fastapi.testclient import TestClient


def test_list_products(client: TestClient):
    respose = client.get("/product/all")
    assert respose.status_code == 200

def test_create_product(client: TestClient):
    data ={"Product Name": "Test Product",
           "price": 1,
           "description":"Demo"}
    response = client.post("/product/add",
                           json=data
                           )
    json_res = response.json()
    assert response.status_code == 200
    assert json_res["price"] == data["price"]