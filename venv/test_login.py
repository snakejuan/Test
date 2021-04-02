import pytest
import requests
from urllib.parse import urljoin

baseurl = "http://localhost:8080"
account_list = [{'userName': 'test1', 'password': '1234'},
                {'userName': 'test2', 'password': '1234'},
                {'userName': 'test3', 'password': '1234'}]


class TestLogin:
    @pytest.mark.parametrize("account",account_list)
    def test_login(self,account):
        url= urljoin(baseurl,"/pinter/bank/api/login2")
        res = requests.post(url=url,data=account)
        print(res.json())
        assert res.json()['data'] is not None