
class TestPage(object):
    def test_home_route(self, client):
        resp = client.get('/')
        print(resp)
        assert b'HELLO WORLD' == resp.data # b specifies byte string
