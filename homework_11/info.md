1. Взять свой код для http://demoqa.com/automation-practice-form
2. Добавить аттачи для Allure – скриншот, page source, console.log и видео
3. Cделать сборку в Jenkins

В качестве ответа на нужно приложить ссылку на Allure-отчет в Jenkins (с видео)

Ссылки:
- На Jenkins - https://jenkins.autotests.cloud/
- На Jenkins Simple - https://jenkins.autotests.cloud/job/teacher-iTerkin-qa_guru_python_9_jenkins_simple/
- На Jenkins DemoQA - https://jenkins.autotests.cloud/job/teacher-iTerkin-qa_guru_python_9_jenkins_demoqa

https://selenoid.autotests.cloud/#/capabilities/


from selenium import webdriver
capabilities = {
"browserName": "chrome",
"browserVersion": "100.0",
"selenoid:options": {
"enableVNC": True,
"enableVideo": False
｝
｝
driver = webdriver. Remote(
command_executor='http://selenoid:4444/wd/hub',)
desired_capabilities=capabilities)