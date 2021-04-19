#!/usr/bin/python3

import os.path
import sublist3r
import subprocess


def parse_domain(domain_name, savefile):
    return sublist3r.main(domain_name,
                          40,
                          savefile,
                          ports=None,
                          silent=False,
                          verbose=False,
                          enable_bruteforce=False,
                          engines=None)


def parse_file(file, output_name):
    with open(file, 'r') as subdom_file:
        data = subdom_file.readlines()
        ips = []
        for domain in data:
            if domain == '' or domain == '\n':
                continue
            command = f'dig {domain[:-1]} +short'
            answer = subprocess.check_output(command.split(' '))
            answer = answer.decode().replace('\n', ' ').split(' ')
            for ip in answer:
                if ip == '' or f'{ip}\n' in ips:
                    continue
                ips.append(f'{ip}\n')
        ips.sort()
        with open('result.txt', 'w+') as res_file:
            res_file.writelines(ips)
            res_file.close()
    subdom_file.close()
    return


def main():
    domain = input('Введите имя домена: ')
    print('Сканирование....')
    format_file = '.txt'
    file = domain.split('.')[0] + format_file
    if file == 'www.txt':
        file = domain.split('.')[1] + format_file
    output_name = file
    if os.path.exists(file):
        parse_file(file, output_name)
        print('Выполнено!')
    else:
        parse_domain(domain, file)
        parse_file(file, output_name)
        print('Выполнено!')


if __name__ == "__main__":
    main()
