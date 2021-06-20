# Truco

## Documentação importante:
[Aqui](https://eduardokatsurayama.atlassian.net/wiki/spaces/T/pages/33012/Truco) você vai encontrar pontos importantes.

## Requisitos:
- Python 3.9.5

## Por onde começar
Clone esse repositório para utilizar como modelo
```sh
git clone git@github.com:Phill-Andrade/truco.git
```

Atualize o remote
```sh
git remote set-url origin git@github.com:Phill-Andrade/truco.git
```

Crie uma branch homolog
```sh
git checkout -b "homolog"
```

Com um virtualenv ativado, instale as dependências:
```sh
pip install -r requirements/dev.txt
```

Crie o .env com base no .env.sample:
```sh
cp contrib/.env.sample .env
```

Execute o script:
```sh
python main.py
```
