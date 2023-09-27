import unittest


class TestCurrencyConversion(unittest.TestCase):

    def test_usd_to_eur_conversion(self):
        # Arrange: Устанавливаем необходимые предусловия и входные данные
        source_currency = "USD"
        target_currency = "EUR"
        amount = 100.0
        currency_rates = {
            "USD": "1.0",
            "EUR": "0.85",
            "RUB": "95.0"
        }

        # Act: Вызываем тестируемую функцию
        result = convert_currency(source_currency, target_currency, amount, currency_rates)

        # Assert: Проверяем, что функция вернула ожидаемый результат
        expected_result = 85.0  # 100 USD = 85 EUR
        self.assertEqual(result, expected_result)


# Запускаем тесты
if __name__ == '__main__':
    unittest.main()
window = TK()
window.resizable(width=True, height=True)
window.title("Конвертер валют")
window.geometry("10x10")
window.mainloop()
