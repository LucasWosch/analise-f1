# 🏎️ F1 EDA – Formula 1 Grand Prix Winners (1950–2025)

Este projeto realiza uma **análise exploratória de dados (EDA)** simples sobre o dataset **Formula 1 Grand Prix Winners Dataset (1950–2025)**, disponível no Kaggle em formato `.csv`.

O sistema foi desenvolvido em **Python**, utilizando **Pandas** para manipulação de dados e **Matplotlib** para visualizações.

---

## 📂 Estrutura

- `main.py` → script principal de análise e geração de gráficos  
- `f1.csv` → dataset 
- `saida_f1/` → pasta onde serão salvos os gráficos gerados  

---

## ▶️ Como executar

1. Execute o script

2. Veja o relatório no **console** e os gráficos salvos em `saida_f1/`.

---

## 📊 Funcionalidades

### 🔹 Leitura e tratamento de dados

* Leitura do CSV com `pandas`
* Conversão de tipos
* Tratamento de valores nulos

### 🔹 Estatísticas descritivas

* Total de corridas
* Período coberto pelo dataset
* Circuitos únicos
* Pilotos e equipes únicas
* Laps médios e mediana
* Duração média e mediana das corridas

### 🔹 Visualizações

Os gráficos são gerados automaticamente e salvos em `saida_f1/`:

* **Top 10 pilotos por vitórias**
* **Quantidade de GPs por ano**

---

## 📑 Exemplo de saída no console

```
=== RELATÓRIO: F1 GRAND PRIX WINNERS (1950–2025) ===
Total de corridas       : 1086
Período coberto         : 1950–2025
Circuitos únicos        : 73
Vencedores únicos       : 112
Equipes únicas          : 57
Laps (média)            : 68.21
Laps (mediana)          : 70.00
Duração média (min)     : 105.87
Duração mediana (min)   : 103.55

Top 10 pilotos por vitórias:
 - Lewis Hamilton: 103
 - Michael Schumacher: 91
 - Sebastian Vettel: 53
 ...
```

py -m pip install --upgrade pip setuptools wheel
py -m pip install "pandas>=2.2" "matplotlib>=3.8"
