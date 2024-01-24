from pytest_mock_resources import create_mongo_fixture
from MongoMock.module import insert_into_customer

mongo = create_mongo_fixture()

def test_insert_into_customer(mongo):
    insert_into_customer(mongo)
    
    collection = mongo['customer']
    returned = collection.find_one()

    assert returned == {"name": "John", "address": "Highway 37"}