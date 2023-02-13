
class TestPage(object):
    def test_home_route(self, client):
        resp = client.get('/')
        assert b'Welcome to ReceiptScanner.' == resp.data # b specifies byte string
