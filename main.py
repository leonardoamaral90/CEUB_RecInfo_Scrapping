import time

from src.functions.status import *
from src.functions.logger import *
from src.functions.scraping import *
from src.functions.file_utils import *
                
def main():
    tamanho_resultado = 250
    pesquisa = [ 'rtx 4060 ti', 'rtx 4070 ti', 'rtx 4080',
                'rx 7800 xt', 'rx 7700 xt', 'rx 7600 xt' ]

    intervalo = 60 * 60 # 60 minutos (1 hora)
    contador = 0

    while True:
        try:
            print(f'Iniciando scrapping em [{len(pesquisa)}] produtos com timeout de [{intervalo} segundos(s)]')
            
            for x in pesquisa:
                print(f'Scrapping no produto [{x}] iniciado!')
                url = f'https://www.kabum.com.br/busca/{x}?page_number=1&page_size={tamanho_resultado}&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched&variant=catalog'
                products = get_price(url)
                products_info = []
                print(f'Foi(ram) encontrado(s) [{len(products)}] anuncios para o produto [{x.upper()}]')
                for product in products:
                    if x.replace(' ', '-') in product['link']:
                        print(product)
                        info = get_product_info(url, product, x)
                        if info:
                            products_info.append(info)

                print(f'Scrapping no produto [{x.upper()}] finalizado!')
                save_log(Status.INFO.name, f'Quantidade de produto(s) encontrado(s) para {x.upper()}: {len(products_info)}')

                list_products = []
                if products_info:
                    for pi in products_info:
                        list_products.append(pi)
                        
                    print(f'Salvando dados coletados do produto [{x.upper()}]!')
                    save_to_file(list_products)
                    print(f'Dados coletados do produto [{x.upper()}] salvo com sucesso!')

            # print(json.dumps(products[0], indent=4))
            # print(json.dumps(products_info[0], indent=4))
            # print(json.dumps(list_products, indent=4))

            print(f'Scrapping finalizado, novo scrapping as [{datetime.datetime.now() + datetime.timedelta(seconds=intervalo)}]!')
            save_log(Status.SUCCESS.name, f'{len(list_products)} dados coletados')
        except Exception as e:
            print(f"Erro ao obter preços dos produtos na Kabum: {e}")
            save_log(Status.ERRO.name, e)
        contador += 1
        time.sleep(intervalo)

if __name__ == "__main__":
    main()