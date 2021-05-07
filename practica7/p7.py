from ftplib import FTP, FTP_PORT
import os, re

def save_file(con: FTP, remote_file_path:str, local_file_path:str):
    with open(local_file_path,'wb') as local_file:
        con.retrbinary(f'RETR {remote_file_path}', local_file.write)

def get_txt_file(con: FTP, file_path:str):
    listado = []
    con.retrlines(f'RETR {file_path}', listado.append)
    return listado

def list_folder(con: FTP, directory:str):
    print(directory)
    listado = []
    con.retrlines(f'LIST {directory}', listado.append)
    return listado

def get_file_dir(con: FTP, directory:str):
    listado = list_folder(con,directory)
    return [file_info for file_info in listado if file_info.startswith('-')],  \
        [file_info for file_info in listado if not file_info.startswith('-')]

def connect_ftp(host, save_path):
    connection = FTP(host)
    connection.login()
    connection.pwd()
    l_file, l_dir = get_file_dir(connection, 'debian')
    #print(f'files:\n{l_file}\ndirs:\n{l_dir}')
    #print(get_txt_file(connection, 'welcome.msg'))
    file_name = 'welcome.msg'
    save_file(connection, file_name, f'{save_path}/{file_name}')
    #print(list_folder(connection, 'debian'))
    connection.cwd('debian')
    connection.retrlines('LIST')
    lista = []
    for x in l_dir:
        exps = re.compile(r"(\w+)$")
        mo = exps.search(x)
        a = str(mo.group(0))
        l_file, l_dir = get_file_dir(connection, a)
        lista.append(l_file)

    with open('ResultadoBusqueda.txt','a+', encoding='utf-8') as a:
        for i in lista:
            for j in i:
                a.write('{}\n'.format(j))

    connection.close()

if __name__ == '__main__':
        connect_ftp('ftp.us.debian.org', 'C:/Users/reymo/Escritorio/Practica7')

 


def get_file_dir(con: FTP, directory:str):
    listado = list_folder(con,directory)
    return [file_info for file_info in listado if file_info.startswith('-')],  \
        [file_info for file_info in listado if not file_info.startswith('-')]

 

def get_file_name(file_info:str) -> str:
    return ''.join(file_info.split()[8:])

 

def connect_ftp(host:str, port:int = FTP_PORT, usr:str = '', pwd:str = '', save_path:str = ''):
    connection = FTP()
    connection.connect(host=host, port=port, timeout=3)
    connection.login(usr,pwd)
    actual_path = ''
    l_file, l_dir = get_file_dir(connection, actual_path)
    files_info = '\n'.join(l_file)
    dirs_info = '\n'.join(l_dir)
    print(f'files:\n{files_info}\ndirs:\n{dirs_info}')
    # print(get_txt_file(connection, 'welcome.msg'))
    # save_file(connection, 'welcome.msg', f'{save_path}/welcome.msg')
    for file_info in l_file:
        file_name = get_file_name(file_info)
        print(file_name)
        save_file(connection, f'{actual_path}/{file_name}', f'{save_path}/{file_name}')
    print(list_folder(connection, 'debian'))

 

    connection.close()

 

if __name__ == '__main__':
    # connect_ftp('192.168.11.3', 8022)
    connect_ftp(host='ftp.mirror.nl', save_path='/home/jhernandez/txt')