from colorama import init, Fore, Style
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from requests import get
from sys import argv, exit
from typing import NoReturn, Optional
from user_agent import generate_user_agent

def error(msg: str, terminate=True) -> NoReturn:
    '''Prints a message an terminate program.'''
#<
    print(f"{Style.BRIGHT}{Fore.RED}[Error]{Style.RESET_ALL} {msg}")
    exit(1)
#>

def info(msg: str) -> None:
    '''Prints an info message.'''
    print(f"{Style.BRIGHT}{Fore.YELLOW}[Info]{Style.RESET_ALL} {msg}")

def get_html(url: str) -> Optional[str]:
    '''Request an url and return it contents.'''
#<
    info(f"Quering '{url}'")
    h: dict = {
        'User-Agent': generate_user_agent()
    }
    info(f"User-Agent: {h['User-Agent']}")
    with get(url, headers=h) as r:
        if r.status_code == 200:
            return r.content
        else:
            error(f"HTTP CODE: {r.status_code}")
#>

def analize_forms(html: str) -> None:
    '''Analize and extracts all forms from an html document'''
#<
    if not html:
        return None
    soup:BeautifulSoup = BeautifulSoup(html, 'lxml')
    ftarget_attrs: list = [
            #<
            'action',
            'enctype',
            'id',
            'method',
            'name',
            'novalidate'
            #>
        ]
    etarget_attrs: list = ['id', 'name', 'type', 'value']

    forms: ResultSet = soup.find_all('form')
    if not forms:
        info(f"{Fore.YELLOW}No forms were found!{Style.RESET_ALL}")
    # loop through forms
    for f in forms:
        # Print all forms attributes
        #<
        print(f"\n{Fore.YELLOW}Form attributes:{Style.RESET_ALL}")
        for fname,fvalue in f.attrs.items():
            # Avoids unimportant attrs
            if fname not in ftarget_attrs:
                continue

            # Converts list into strings
            if isinstance(fvalue, list):
                fvalue = " ".join(fvalue)

            print(f"- {Fore.RED}{fname}: {Style.RESET_ALL}{fvalue}")
        #>

        # Extract form elements
        elements: ResultSet = f.find_all([
            #<
                'a',
                'input',
                'textarea',
                'select',
                'button'
            #>
            ])

        # loop through elements
        for e in elements:
            # Print all elements attributes
            #<
            print(f"- {Fore.YELLOW}{e.name.capitalize()} attributes: {Style.RESET_ALL}")
            for ename,evalue in e.attrs.items():
                # Avoids unimportant attrs
                if ename not in etarget_attrs:
                    continue

                # Converts list into strings
                if isinstance(evalue, list):
                    evalue = " ".join(evalue)

                print(f"-- {Fore.RED}{ename}:{Style.RESET_ALL} {evalue}")
            #>

#>

def main():
#<
    # Validar parámetro cli URL
    if len(argv) == 1:
        error("URL not given!")

    url = argv[1]

    # Obtener HTML
    html = get_html(url)
    if not html:
        error("Can't get an html response!")

    # Analizar forms
    analize_forms(html)
#>

if __name__ == '__main__':
    main()
