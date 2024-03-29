from datetime import datetime
from pymongo.mongo_client import MongoClient
from MongoMock.fixtures import mongo_client_fixture
from MongoMock.crud import insert_user

use_fixtures = [mongo_client_fixture]


def test_insert_user(conn: MongoClient):
    # 建立假資料
    data = {"username": "wiwi_kuo",
            "email": "wiwi_kuo@migocorp.com",
            "birthday": datetime(year=2022, month=12, day=31)}
    
    # 測試 CRUD 方法
    result = insert_user(data=data, conn=conn)
    print(result)
    
    # 驗證內容
    assert result["username"] == data["username"]
    assert result["email"] == data["email"]
    assert result["birthday"] == data["birthday"]