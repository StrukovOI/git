Создание ключа:
ssh-keygen -t ed25519 -C "your_email@example.com"

Добавление ключа в ssh-агент:
eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/приватный ключ