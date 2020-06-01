Title: Como utilizar argumentos via bash em um script python
Slug: utilizar-argumentos-script-python
Date: 2020-05-31 22:35
Category: python
Tags: python, script, parser
Author: Lucas Emanuel
Summary: Prosseguindo com as dicas em Python, esse post vem responder: **"Da pra utilizar argumentos via bash em um script python?"**

Prosseguindo com as dicas em Python, esse post vem responder ao questionamento: **"Da pra utilizar argumentos via bash em um script python?"**. Adianto que: Sim! Então, vem comigo até o fim!

Aprender a executar um script/aplicação através de um bash(terminal, cmd, powershell), utilizando argumentos como entrada é uma das coisas mais funcionais a serem aprendidas na vida de quem desenvolve.

Geralmente, durante a vida acadêmica, poucas vezes isso nos é demonstrado e muito menos nos é dito todo o seu pontencial de uso. 

E, em poucos exemplos, através desse modo de execução pode-se fazer coisas como:

- Agendar/Automatizar uma execução
- Realizar execuções condicionais
- Utilizar outros scripts para 'disparar' uma execução
- E por aí vai... 

Cabe a você descobrir pra que precisa e como aplicar.

Vamos lá, vou lhe mostrar utilizando como exemplo o código que geramos no post sobre como [Transformar json em arquivo CSV com Python](https://lucasebs.github.io/posts/2020/05/json-to-csv-python/) (se não leu, se ligue!):

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

Vamos chamá-lo de `script_feliz_transforma_json_em_csv.py`!

------------------------------

## Está começando a desenvolver a pouco tempo?

> ##### Nota!
> Caso esteja apenas buscando como fazer, segue que mais embaixo já tem mostrando como. 

**Mas...** Se você desenvolve a pouco tempo e/ou nunca explorou esse mundo de argumentos, lhe explico.

Bem, se fossemos executar nosso script via bash utilizaríamos:

```bash
$ python script_feliz_transforma_json_em_csv.py
```

Até então tudo ok! Mas qual seria o problema disso? 

- Imagine que tivesse diversos arquivos para transformar de json para csv. 
- Agora, imagine abrir o `script_feliz_transforma_json_em_csv.py` a cada arquivo e alterar o nome do arquivo de entrada e saída para cada caso. Não seria tão legal, né?

E se você pudesse, ainda na execução, 'informar' ao seu script o arquivo a ser tranformado, além do nome do arquivo csv gerado?  

Seria bem mais rápido do que ter que mudar dentro do script, né?

Pois bem, isso seria passar os nome dos arquivos como argumentos para seu script e seria mais ou menos assim:

```bash
$ python script_feliz_transforma_json_em_csv.py file.json file.csv
```

Agora segue, que vou ensinar como fazer isso ligeirinho!

------------------------------

## Como fazer isso e tal?

Utilizaremos apenas uma biblioteca python, `sys`.

```python
import sys
```

Show! Tudo o que é passado como argumento para um script python ficará registrado em uma lista ~~python~~ que pode ser acessada em `sys.argv`

Por exemplo, se tivéssemos o seguinte script `argumentos.py`:

```python
import sys

print(sys.argv)
```

E executássemos passando os seguintes argumentos:

```bash
$ python argumentos.py oi lindos do meu coracao
```

Teríamos como saída:

    ['oi', 'lindos', 'do', 'meu', 'coracao']

Sabendo disso, poderíamos acessar qualquer elemento como acessamos os elementos de qualquer lista em python. Onde, no exemplo acima poderíamos utilizar:

```python
print(sys.argv[0], sys.argv[4])
```

Para obter:

    oi coração

Assim, em nosso `script_feliz_transforma_json_em_csv.py`, teríamos de, inicialmente, importar a biblioteca `sys`

```python
import sys, csv, json
```

E alterar onde iríamos receber cada argumento no nosso script, considerando que:

1. O primeiro argumento recebido seria o arquivo json
2. O segundo argumento seria o arquivo de saída, transformado para csv

Então teríamos de incluir o argumento para o nosso arquivo json, o primeiro argumento:

```python
file_json = open(sys.argv[0])
json_data = json.load(file_json)
file_json.close()
```

E também o nosso arquivo csv de saída, o segundo argumento:

```python
file_csv = open(sys.argv[1], 'w')
output_csv = csv.writer(file_csv)
```

**E só!**

Por fim, teremos nosso script `script_feliz_transforma_json_em_csv.py`:

```python
import sys, csv, json

file_json = open(sys.argv[0])
json_data = json.load(file_json)
file_json.close()

file_csv = open(sys.argv[1], 'w')
output_csv = csv.writer(file_csv)
output_csv.writerow(json_data[0].keys())

for row in json_data:
    output_csv.writerow(row.values())
file_csv.close()
```

E, assim, podemos executá-lo:

```bash
$ python script_feliz_transforma_json_em_csv.py file_entrada.json file_saida.csv
```

E é só isso mesmo, de verdade! 

> ##### Nota! 
> Maioria das linguagens de programação fazem uso desta mesma funcionalidade. Basta também pesquisar como fazer e ser feliz.

Pronto, agora é explorar as formas de como utilizar da maneira que for mais funcional para as suas necessidades! 

Xero no coração!

------

### Aviso

Essa página não nasceu pra ser "a luz, a verdade e a vida", onde tudo é diferenciado, muitas coisas poderão ser encontradas facilmente pelo restante da internet (como quase tudo), mas quem sabe aqui não seja um caminho de referência fácil?! 


#### Gostou? Tá com dúvida?

Chama no comentário aqui embaixo! (Ou reage feliz com amorzinho! <3)