server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_key in server_data:
    print('{key}:'.format(key=i_key))
    for j_key, j_value in server_data[i_key].items():
        print('\t{0}: {1}'.format(j_key, j_value))
