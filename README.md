# 🤖 Automação de Cadastro de Produtos

Script em Python que automatiza o cadastro de produtos em um sistema web da empresa. Ele abre o navegador, faz login, lê uma base de dados em CSV e cadastra cada produto, um por um, simulando as ações de uma pessoa com mouse e teclado.

## 📋 Sobre o projeto

Cadastrar dezenas ou centenas de produtos manualmente é um trabalho repetitivo e propenso a erros. Este projeto resolve isso automatizando todo o processo:

1. Abre o Google Chrome e acessa o sistema da empresa
2. Realiza o login
3. Importa a base de dados (`produtos.csv`)
4. Cadastra um produto
5. Repete o passo 4 até acabar a lista

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/): controle de mouse e teclado
- [Pandas](https://pandas.pydata.org/): leitura e manipulação da base de dados

## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- Sistema operacional Windows (o script usa a tecla `win` para abrir o menu iniciar)

## 🚀 Instalação

Baixe os arquivos do projeto e instale as dependências:

```bash
pip install pyautogui pandas
```

## 📁 Base de dados

O arquivo `produtos.csv` incluído neste repositório serve apenas como exemplo, para você ver como a base de dados deve ser organizada. Você pode substituí-lo pelos seus próprios produtos, desde que mantenha o mesmo nome e as mesmas colunas.

O arquivo deve estar na mesma pasta do script e conter as seguintes colunas:

| Coluna            | Descrição                          |
|-------------------|------------------------------------|
| `codigo`          | Código do produto                  |
| `marca`           | Marca                              |
| `tipo`            | Tipo do produto                    |
| `categoria`       | Categoria                          |
| `preco_unitario`  | Preço unitário                     |
| `custo`           | Custo do produto                   |
| `obs`             | Observações (opcional)             |

Exemplo:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
1001,Marca A,Tipo X,1,25.90,10.50,
1002,Marca B,Tipo Y,2,49.90,22.00,Produto em promoção
```

## ▶️ Como usar

1. Preencha suas credenciais de login no script (campos de e-mail e senha).
2. Garanta que o arquivo `produtos.csv` está na mesma pasta do script.
3. Execute o script:

```bash
python main.py
```

4. **Não mexa no mouse nem no teclado** enquanto a automação estiver rodando.

> 💡 Para interromper a execução em caso de emergência, mova o mouse rapidamente para o canto superior esquerdo da tela. O PyAutoGUI possui esse *fail-safe* ativado por padrão.

## 🔧 Configurações importantes

O script usa **coordenadas fixas de tela** para clicar nos campos (por exemplo, `x=834, y=401` para o campo de e-mail e `x=822, y=300` para o campo de código). Como cada monitor tem uma resolução diferente, talvez seja necessário ajustar esses valores.

Para descobrir a posição do mouse na sua tela:

```python
import pyautogui
import time

time.sleep(5)
print(pyautogui.position())
```

Além disso, os tempos de espera (`time.sleep`) podem precisar de ajuste conforme a velocidade da sua internet e do seu computador.

## 🔒 Segurança

**Nunca envie suas credenciais reais para o GitHub.** O ideal é armazenar e-mail e senha em variáveis de ambiente ou em um arquivo `.env` (adicionado ao `.gitignore`), em vez de deixá-los escritos diretamente no código.

## ⚠️ Limitações

- Depende da resolução e do layout da tela
- Depende da ordem dos campos (navegação por `Tab`) do sistema
- A automação não deve ser interrompida nem usada em paralelo com outras atividades no computador

## 📚 Créditos

Projeto desenvolvido como parte do curso Python Impressionador, da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/).

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
