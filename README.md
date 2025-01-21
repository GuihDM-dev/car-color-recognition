# **Identificação de Cores de Carros com YOLOv8**

Este é um projeto de detecção e classificação de cores de carros utilizando o modelo YOLOv8, treinado com o dataset **VCoR (Vehicle Color Recognition)**. A interface permite carregar imagens de veículos e obter as predições das cores detectadas.

## **Demonstração**
Uma interface simples e funcional foi desenvolvida para este projeto, utilizando **Streamlit**.  
Você pode fazer o upload de uma imagem para detectar os veículos e suas respectivas cores.

---

## **Funcionalidades**
- Detecção de veículos em imagens.
- Identificação da cor predominante de cada veículo.
- Visualização de predições diretamente na imagem carregada.
- Exibição de métricas de desempenho, como confiança e classes detectadas.

---

## **Tecnologias Utilizadas**
- **YOLOv8**: Framework de deep learning para detecção de objetos.
- **Streamlit**: Ferramenta para criar uma interface web interativa.
- **Python**: Linguagem principal do projeto.
- **Pandas & Matplotlib**: Para análise e visualização dos dados de treinamento.
- **VCoR Dataset**: Dataset utilizado para treinar o modelo, contendo informações de cores e classes de veículos.

---

## **Como Executar o Projeto**

### **Pré-requisitos**
Certifique-se de ter as seguintes dependências instaladas:
- Python 3.8 ou superior
- Bibliotecas: `ultralytics`, `streamlit`, `torch`, `PIL`

Instale as dependências com:
pip install -r requirements.txt

### Passos para Execução
Clone este repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Execute Todo o codigo no google collab


### Exemplo de Uso
Carregue uma imagem contendo veículos.
Aguarde o processamento do modelo.
Veja a imagem anotada com os veículos detectados e suas cores, além de métricas como confiança.

### Contribuições são bem-vindas! Sinta-se à vontade para:
Abrir issues com sugestões ou melhorias.
Submeter pull requests com novas funcionalidades ou correções.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
