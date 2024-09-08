# Rede Bayesiana para Previsão de Condições Médicas

Este projeto utiliza Redes Bayesianas para modelar e prever a probabilidade de uma condição médica, como diabetes, usando um conjunto de dados médicos. A biblioteca `pgmpy` é empregada para construir e inferir a Rede Bayesiana.

## Funcionalidades

- **Construção da Rede Bayesiana**: Definição da estrutura da rede com base nas variáveis fornecidas.
- **Aprendizado de Parâmetros**: Uso de técnicas como Estimador de Máxima Verossimilhança para aprender os parâmetros da rede.
- **Inferência e Predição**: Realização de inferências para prever a probabilidade de uma condição médica com base em características.
- **Validação e Avaliação**: Validação da acurácia do modelo usando técnicas de validação cruzada.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python: `pgmpy`, `pandas`, `numpy`

## Instalação

Siga os passos abaixo para configurar e rodar a aplicação localmente.

### 1. Clone o Repositório

```bash```
git clone https://github.com/seu_usuario/nome_do_repositorio.git
cd nome_do_repositorio

2. Crie e Ative um Ambiente Virtual (Recomendado)
No Windows:

```bash```
Copiar código
python -m venv venv
venv\Scripts\activate
No macOS/Linux:

```bash```
Copiar código
python3 -m venv venv
source venv/bin/activate

3. Instale as Dependências
Crie um arquivo requirements.txt com o seguinte conteúdo e instale as dependências:
Copiar código
pgmpy
pandas
numpy

Instale as dependências com:
```bash```
Copiar código
pip install -r requirements.txt

4. Prepare o Conjunto de Dados:
Certifique-se de que o conjunto de dados está no formato esperado e localizado corretamente.

5. Execute o Script:
```bash```
Copiar código
python bayesianas_dados_medicos.py
Estrutura do Projeto
```bash```
Copiar código

.
├── bayesianas_dados_medicos.py  # Script principal para construção e inferência da Rede Bayesiana
├── requirements.txt             # Lista de dependências do projeto
└── README.md                    # Instruções e documentação do projeto
Dependências
pgmpy: Biblioteca para construção e inferência de Redes Bayesianas.
pandas: Biblioteca para manipulação e análise de dados.
numpy: Biblioteca para operações numéricas.
Problemas Comuns
Se você encontrar erros relacionados à alocação de memória, considere simplificar a estrutura da rede ou o conjunto de dados. Verifique se você está usando versões compatíveis das bibliotecas pgmpy, pandas, e numpy.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Nota: Substitua https://github.com/seu_usuario/nome_do_repositorio.git pelo URL real do seu repositório e ajuste os caminhos e nomes de arquivos conforme necessário.

go
Copiar código

Esse `README.md` assume que você tem um único script e um arquivo `requirements.txt`. Ajuste conforme necessário 
