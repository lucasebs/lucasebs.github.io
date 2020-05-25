Title: Transformar dados json em arquivo CSV
Slug: json-to-csv-python
Date: 2020-05-25 00:28
Category: python
Tags: python, pandas, json, csv
Author: Lucas Emanuel
Summary: Pra começar, já no primeiro post, segue a(s) resposta(s) da seguinte pergunta: **"Como salvar um json em um arquivo csv?"**

Pra começar, já no primeiro post, logo com a resposta da seguinte pergunta: **"Como é que eu faço pra salvar um json em um arquivo csv?"**

No contexto dessa pergunta seria para aplicar em Node.js (o que eu realmente nunca tinha feito), mas em Python eu sabia bem como fazer. E basicamente vou dividir em duas maneira: Profissional e Estudante(fica até o final que vai dar bom!).

## Maneira 1 - Profissional

A maneira profissional é como você utilizará pra solucionar um problema rápido, afim de obter o resultado da melhor maneira possível e isso requer bem menos recursos e lógicas

Inicialmente utilizaremos duas bibliotecas de python `csv` e `json`

```python
import csv, json
```
Em seguida, basta carregar o json em uma variável, neste caso a linda `json_data`, partindo de um arquivo `file_name.json`

```python
file_json = open('file_name.json')
json_data = json.load(file_json)
file_json.close()
```

Agora que possuímos os dados em json, podemos criar nosso `file_name.csv`, bem como um *writer* para escrever os dados nos arquivos.

```python
file_csv = open('file_name.csv', 'w')
output_csv = csv.writer(file_csv)
```

Para escrever nossos *headers* precisaremos apenas chamar a função `writerow()` e passar como parâmetro a lista com as *keys* do arquivo json a serem utilizados como *headers*


```python
output_csv.writerow(json_data[0].keys())
```

Iterando em cada elemento do `json_data`, conseguimos escrever nossos dados no maravilhoso `file_name.csv`, ao passar como parâmetro da função `writerow()` os valores do elemento, que podem ser obtidos através da função `values()`


```python
for row in json_data:
        output_csv.writerow(row.values())
```

Por fim, nunca esquecer de fechar o arquivo em que terminamos de escrever.

```python
file_csv.close()
```

E fim! O código inteiro fica da seguinte forma:

```python
import csv, json

file_json = open('file_name.json')
json_data = json.load(file_json)
file_json.close()

file_csv = open('file_name.csv', 'w')
output_csv = csv.writer(file_csv)
output_csv.writerow(json_data[0].keys())

for row in json_data:
    output_csv.writerow(row.values())
file_csv.close()
```

#### Em 2 linhas de código!!!!

Caso não queira ter nenhum trabalho, basta utilizar a biblioteca pandas.


> Para saber mais sobre a biblioteca pandas acesse: <https://pandas.pydata.org/>



E fazer todo esse trabalho em 2 linhas 

```python
import pandas as pd
pd.read_json (r'file_name.json').to_csv (r'file_name.csv', index = None)
```

A primeira linha importa a biblioteca, a segunda,lê o json a partir do arquivo `file_json.json` e transforma os dados lidos escrevendo no arquivo `file_name.csv`


> ##### Nota! 
Dados em Json podem estar formatados de maneiras diferentes. Para conseguir ler cada uma dessas maneiras recomendo [acessar a documentação específica da função `read_json()` do pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)


## Maneira 2 - Estudante 

Chamei esta maneira como "Estudante" devido a alguns momentos enquanto estudantes em que é preciso compreender como as coisas funcionam e como seriam implementadas(E talvez você até precise implementar), então se for este o caso, segue aí e 'vamo ser feliz'!

> ##### Nota!

> Não necessariamente quer dizer que não seja profissional, ou não deva sem implementado desta maneira, mas deve sempre ser levado em consideração que essa implementação exigido um relativo custo computacional, principalmente quando for preciso lidar com grandes volumes de dados.

#### O Json
 
Para transformar os dados dessa estrutura abaixo, `json_example`, em um arquivo precisaremos percorrer cada um deles e escrever no nosso querido `file.csv`.

```python
json_example = [{'Series': 'I', 'X': 10.0, 'Y':8.04},
 {'Series': 'I', 'X': 8.0, 'Y': 6.95},
 {'Series': 'I', 'X': 13.0, 'Y': 7.58},
 {'Series': 'I', 'X': 14.0, 'Y': 9.96},
 {'Series': 'II', 'X': 10.0, 'Y': 9.14},
 {'Series': 'II', 'X': 8.0, 'Y': 8.14},
 {'Series': 'II', 'X': 13.0, 'Y': 8.74},
 {'Series': 'II', 'X': 9.0, 'Y': 8.77},
 {'Series': 'III', 'X': 10.0, 'Y': 7.46},
 {'Series': 'III', 'X': 8.0, 'Y': 6.77},
 {'Series': 'III', 'X': 13.0, 'Y': 12.74},
 {'Series': 'III', 'X': 9.0, 'Y': 7.11},
 {'Series': 'IV', 'X': 8.0, 'Y': 6.58},
 {'Series': 'IV', 'X': 8.0, 'Y': 5.76},
 {'Series': 'IV', 'X': 8.0, 'Y': 7.71},
 {'Series': 'IV', 'X': 8.0, 'Y': 8.84}]
```

Um json de forma básica é uma estrutura de chaves e valores, onde pra cada chave de um elemento você terá um valor.

#### O CSV

Um arquivo csv é um arquivo de texto onde cada coluna é determinada por um separador específico, podendo ser ponto e vírgula `;`,  vírgula`,` e até mesmo um TAB `\t` ou um espaço em branco `  `.

Sendo assim, nosso arquivo final deverá parecer mais ou menos assim:

    Series;X;Y
    I;10.0;8.04
    I;8.0;6.95
    I;13.0;7.58
    I;14.0;9.96
    II;10.0;9.14


#### Escrevendo no arquivo csv

Antes de qualquer coisa, vamos criar uma variável que vai armazenar todo o conteúdo a ser gravado no nosso `file.csv`. E então poderemos seguir. 

```python
string_content = ''
```

Geralmente um arquivo csv possue *headers* (cabeçalhos), para melhor entendimento do que cada coluna carrega de dados. 

Pois bem, pensando nisso, e olhando para o lindo `json_example`, cada *key* (chave) seria um bom *header* para nosso `file.csv`, então vamos obter isso.

Através da função `keys()` obteremos as keys do primeiro elemento, do `json_example`.


```python
keys = json_example[0].keys()
keys
```

    dict_keys(['Series', 'X', 'Y'])


Iremos começar iterando sobre a lista de keys com a função `enumerate()`. Ela irá retornar duas informações a posição do valor na lista e o próprio valor.


```python
for i, k in enumerate(keys):
```

Iremos guardar cada valor na variável `string_content` separada por um `;`. Mas para sabermos onde parar e seguir pra linha seguinte, valor incluir uma lógica que irá verificar se a posição do valor é menor que a última posição da lista. Se for menor, incluirá antes do próximo valor o separador `;`, se não, irá incluir uma quebra de página `\n`. Por fim teremos:


```python
for i, k in enumerate(keys):
    string_content += k
    if (i < len(keys)-1):
        string_content += ';'
    else:
        string_content += '\n'
```

Por fim já teremos nossos *headers*


```python
string_content
```




    'Series;X;Y\n'



Seguiremos a mesma lógica, mas apenas percorrendo em cada um dos elementos do json.


```python
for j in json_example:
    for i, key in enumerate(j.keys()):
        string_content += str(j[key])
        if (i < len(keys)-1): 
            string_content += ';'
        else:
            string_content += '\n'
```

E fim! Já temos tudo pronto, sem dores.


```python
string_content
```




    'Series;X;Y\nI;10.0;8.04\nI;8.0;6.95\nI;13.0;7.58\nI;14.0;9.96\nII;10.0;9.14\nII;8.0;8.14\nII;13.0;8.74\nII;9.0;8.77\nIII;10.0;7.46\nIII;8.0;6.77\nIII;13.0;12.74\nIII;9.0;7.11\nIV;8.0;6.58\nIV;8.0;5.76\nIV;8.0;7.71\nIV;8.0;8.84\n'



Calma que não fica tão feio assim, no nosso `file.csv` teremos este resultado


```python
print(string_content)
```

    Series;X;Y
    I;10.0;8.04
    I;8.0;6.95
    I;13.0;7.58
    I;14.0;9.96
    II;10.0;9.14
    II;8.0;8.14
    II;13.0;8.74
    II;9.0;8.77
    III;10.0;7.46
    III;8.0;6.77
    III;13.0;12.74
    III;9.0;7.11
    IV;8.0;6.58
    IV;8.0;5.76
    IV;8.0;7.71
    IV;8.0;8.84
    


Para finalmente escrever no nosso `file.csv`, basta 3 linhas


```python
file = open("file.csv", "w")
file.write(string_content)
file.close()
```

E é isso! Embora pareça muito, nosso código final fica assim:

```python
json_example = [{'Series': 'I', 'X': 10.0, 'Y': 8.04},
 {'Series': 'I', 'X': 8.0, 'Y': 6.95},
 {'Series': 'I', 'X': 13.0, 'Y': 7.58},
 {'Series': 'I', 'X': 14.0, 'Y': 9.96},
 {'Series': 'II', 'X': 10.0, 'Y': 9.14},
 {'Series': 'II', 'X': 8.0, 'Y': 8.14},
 {'Series': 'II', 'X': 13.0, 'Y': 8.74},
 {'Series': 'II', 'X': 9.0, 'Y': 8.77},
 {'Series': 'III', 'X': 10.0, 'Y': 7.46},
 {'Series': 'III', 'X': 8.0, 'Y': 6.77},
 {'Series': 'III', 'X': 13.0, 'Y': 12.74},
 {'Series': 'III', 'X': 9.0, 'Y': 7.11},
 {'Series': 'IV', 'X': 8.0, 'Y': 6.58},
 {'Series': 'IV', 'X': 8.0, 'Y': 5.76},
 {'Series': 'IV', 'X': 8.0, 'Y': 7.71},
 {'Series': 'IV', 'X': 8.0, 'Y': 8.84}]

keys = json_example[0].keys()

string_content = ''

for i, k in enumerate(keys):
    string_content += k
    if (i < len(keys)-1):
        string_content += ';'
    else:
        string_content += '\n'

for j in json_example:
    for i, key in enumerate(j.keys()):
        string_content += str(j[key])
        if (i < len(keys)-1): 
            string_content += ';'
        else:
            string_content += '\n'

file = open("file.csv", "w")
file.write(string_content)
file.close()
```




### Aviso

Essa página não nasceu pra ser "a luz, a verdade e a vida", onde tudo é diferenciado, muitas coisas poderão ser encontradas facilmente pelo restante da internet(como quase tudo), mas quem sabe aqui não seja um caminho de referência fácil? 


#### Gostou? Tá com dúvida?

Chama no comentário aqui embaixo! (Ou reage feliz com amorzinho! <3)