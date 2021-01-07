### to run use 2 terminals:
####migrate first
`
./manage.py runserver
`
and
`
./manage.py qcluster
`

## Джанго приложение. Используется Django_q для асинхронной обработки данных.

## django_q использует AWS SQS очередь при сериализации задания.

## При регистрации отправляется сообщение ил через GMAIL SMTP, или AWS SES.

## Фото сохранияется в AWS S3 bucket.

## При загрузки на AWS S3, AWS Lambda код на питоне уменьшает размеры фото.
### Триггером является AWS SQS напрямую

## AWS очередь -> при написании жалобы

## для использования AWS нужно убрать комменты `# commented for testing styling`