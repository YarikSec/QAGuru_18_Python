1) Метод api_request лучше сделать статичным (добавить @staticmethod перед методом), тк экземпляр класса не передается в него

2) Чтобы абракадабры не было в логах нужно поправить 2 кусочка
### вместо
```
allure.attach(
body=json.dumps(result.text, indent=4, ensure_ascii=True),
name="Response",
attachment_type=AttachmentType.JSON,
extension="json",
)
```

### вставляем этот блок
```
try:
response_json = result.json() # Пытаемся парсить как JSON
allure.attach(
body=json.dumps(response_json, indent=4, ensure_ascii=False),
name="Response",
attachment_type=AttachmentType.JSON,
extension="json"
)
except ValueError: # Если не JSON, сохраняем как текст
allure.attach(
body=result.text,
name="Response",
attachment_type=AttachmentType.TEXT,
extension="txt"
)
```

### аналогично для логов в консоли:
#### вместо
```
logging.info(result.text)
```
#### вставляем эту строчку
```
logging.info(f'{json.dumps(json.loads(result.text), indent=4, ensure_ascii=False) if result.text else "None"}')
```

3) папки в питоне принято называть с маленькой буквы -> aqa_api_demowebshop