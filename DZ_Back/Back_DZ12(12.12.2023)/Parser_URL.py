with open("URL.txt", "r") as file:
    urls = file.readlines()


for url in urls:
    parts = url.strip().split('://')
    protocol = parts[0] if len(parts) > 1 else None

    parts = parts[-1].split('/', 1)
    domain = parts[0]

    path = ''
    params = {}

    if len(parts) > 1:
        parts = parts[-1].split('?')
        path = '/' + parts[0]

        if len(parts) > 1:
            params_list = parts[-1].split('&')
            for param in params_list:
                key_value = param.split('=')
                params[key_value[0]] = key_value[1]


    print("Протокол:", protocol)
    print("Доменное имя:", domain)
    print("Запрос:", path)
    print("Параметры:")
    for key, value in params.items():
        print(f"   {key} = {value}")