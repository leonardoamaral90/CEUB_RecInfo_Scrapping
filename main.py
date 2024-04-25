import time
import datetime
from src.functions.status import *
from src.functions.logger import *
from src.functions.scraping import *
from src.functions.file_utils import *
                
def main():
    # Tamanho máximo de resultados por pesquisa
    tamanho_resultado = 250
    # Lista de produtos para pesquisar
    pesquisa = [ 'rtx 4060 ti', 'rtx 4070 ti', 'rtx 4080',
                'rx 7800 xt', 'rx 7700 xt', 'rx 7600 xt' ]
    # Intervalo de tempo entre as pesquisas (em segundos)
    intervalo = 60 * 60  # 1 hora
    contador = 0

    # Loop principal
    while True:
        try:
            print(f'Iniciando scrapping em [{len(pesquisa)}] produtos com timeout de [{intervalo} segundos(s)]')
            
            # Itera sobre cada item na lista de pesquisa
            for x in pesquisa:
                print(f'Scrapping no produto [{x}] iniciado!')
                # URL da pesquisa para o produto atual
                url = f'https://www.kabum.com.br/busca/{x}?page_number=1&page_size={tamanho_resultado}&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched&variant=catalog'
                # Obtém os preços dos produtos na página de pesquisa
                products = get_price(url)
                # Lista para armazenar informações dos produtos encontrados
                products_info = []
                print(f'Foi(ram) encontrado(s) [{len(products)}] anuncios para o produto [{x.upper()}]')
                # Itera sobre cada produto encontrado
                for product in products:
                    # Verifica se o link do produto contém o nome do produto na pesquisa
                    if x.replace(' ', '-') in product['link']:
                        print(product)
                        # Obtém informações detalhadas do produto
                        info = get_product_info(url, product, x)
                        if info:
                            products_info.append(info)

                print(f'Scrapping no produto [{x.upper()}] finalizado!')
                # Registra o número de produtos encontrados no log
                save_log(Status.INFO.name, f'Quantidade de produto(s) encontrado(s) para {x.upper()}: {len(products_info)}')

                list_products = []
                # Se houver informações de produtos, adiciona à lista
                if products_info:
                    for pi in products_info:
                        list_products.append(pi)
                        
                    print(f'Salvando dados coletados do produto [{x.upper()}]!')
                    # Salva os dados coletados em um arquivo
                    save_to_file(list_products)
                    print(f'Dados coletados do produto [{x.upper()}] salvo com sucesso!')

            print(f'Scrapping finalizado, novo scrapping as [{datetime.datetime.now() + datetime.timedelta(seconds=intervalo)}]!')
            # Registra no log o sucesso na coleta de dados
            save_log(Status.SUCCESS.name, f'{len(list_products)} dados coletados')
        except Exception as e:
            print(f"Erro ao obter preços dos produtos na Kabum: {e}")
            # Registra no log o erro ocorrido
            save_log(Status.ERRO.name, e)
        contador += 1
        # Aguarda o intervalo de tempo antes de fazer a próxima pesquisa
        time.sleep(intervalo)

if __name__ == "__main__":
    main()
