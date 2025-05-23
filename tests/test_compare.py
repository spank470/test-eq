import requests
import allure

@allure.suite("Сравнение HTML-ответов с двух серверов")  # Название группы в Allure
class TestCompareHTML:

    @allure.title("1 - web_tour")
    @allure.description("Проверяем, что страницы REF и TARGET возвращают одинаковый HTML и статус код 200.")
    def test_compare_html_web_tour(self):
        url_ref = "http://webtours.load-test.ru:1090/cgi-bin/nav.pl?in=home"
        url_target = "http://webtours.load-test.ru:1090/cgi-bin/nav.pl?in=home"

        with allure.step(f"GET запрос к REF: {url_ref}"):
            ref = requests.get(url_ref)
            allure.attach(ref.text, name="REF Response", attachment_type=allure.attachment_type.TEXT)
            assert ref.status_code == 200

        with allure.step(f"GET запрос к TARGET: {url_target}"):
            target = requests.get(url_target)
            allure.attach(target.text, name="TARGET Response", attachment_type=allure.attachment_type.TEXT)
            assert target.status_code == 200

        with allure.step("Сравнение HTML содержимого"):
            assert ref.text == target.text, "HTML ответы отличаются!"

    @allure.title("2 - google")
    @allure.description("Проверяем, что страницы REF и TARGET возвращают одинаковый HTML и статус код 200.")
    def test_compare_html_google(self):
        url_ref = "http://webtours.load-test.ru:1090/cgi-bin/nav.pl?in=home"
        url_target = "http://google.com"

        with allure.step(f"GET запрос к REF: {url_ref}"):
            ref = requests.get(url_ref)
            allure.attach(ref.text, name="REF Response", attachment_type=allure.attachment_type.TEXT)
            assert ref.status_code == 200

        with allure.step(f"GET запрос к TARGET: {url_target}"):
            target = requests.get(url_target)
            allure.attach(target.text, name="TARGET Response", attachment_type=allure.attachment_type.TEXT)
            assert target.status_code == 200

        with allure.step("Сравнение HTML содержимого"):
            assert ref.text == target.text, "HTML ответы отличаются!"
            
    @allure.title("3 - yandex")
    @allure.description("Проверяем, что страницы REF и TARGET возвращают одинаковый HTML и статус код 200.")
    def test_compare_html_yandex(self):
        url_ref = "http://yandex.ru"
        url_target = "http://google.com"

        with allure.step(f"GET запрос к REF: {url_ref}"):
            ref = requests.get(url_ref)
            allure.attach(ref.text, name="REF Response", attachment_type=allure.attachment_type.TEXT)
            assert ref.status_code == 200

        with allure.step(f"GET запрос к TARGET: {url_target}"):
            target = requests.get(url_target)
            allure.attach(target.text, name="TARGET Response", attachment_type=allure.attachment_type.TEXT)
            assert target.status_code == 200

        with allure.step("Сравнение HTML содержимого"):
            assert ref.text == target.text, "HTML ответы отличаются!"
            

            
            