import requests



class Test_API_Response:


    def test_server_available(self):
        response = requests.get("https://jsonplaceholder.typicode.com/")
        assert response.status_code == 200, "Неверный статус код"

    def test_response_have_body(self):
        response = requests.get("https://jsonplaceholder.typicode.com/")
        assert response.content is not None, "Пустое тело ответа"