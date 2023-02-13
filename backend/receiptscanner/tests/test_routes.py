
class TestPage(object):
    def test_home_route(self, client):
        resp = client.get('/')
        assert b'Welcome to Receipt5canner.' == resp.data # b specifies byte string
