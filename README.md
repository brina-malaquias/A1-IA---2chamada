# A1-IA---2chamada
# MLP – Problema de Paridade de 3 Bits

## 📋 Descrição do Projeto

Este repositório contém a implementação e análise de uma Rede Neural Multicamadas (MLP) aplicada ao problema lógico da **paridade de 3 bits**. O objetivo é investigar como diferentes combinações de hiperparâmetros afetam:

- A velocidade de convergência (número de épocas até estabilização do erro).
- O valor do erro médio quadrático final (MSE).
- Possíveis instabilidades ou estagnações no aprendizado.

---

## 🔧 Metodologia

- **Arquitetura**  
  - Camada de entrada: 3 neurônios (cada bit).  
  - Camada oculta: variável (2, 3, 4 ou 6 neurônios).  
  - Camada de saída: 1 neurônio (saída binária).  
- **Função de ativação**: Sigmoid  
- **Função de perda**: Mean Squared Error (MSE)  
- **Otimização**: Gradient Descent (learning rate customizável)  
- **Dados de treinamento**: Todas as 8 combinações possíveis de 3 bits  
  - Saída = 1 se o número de bits “1” for ímpar  
  - Saída = 0 se for par  

---

## ⚙️ Hiperparâmetros Testados

| Exp | Neurônios (oculta) | Learning Rate | Épocas | Observações gerais                  |
|-----|--------------------|---------------|--------|-------------------------------------|
| 1   | 2                  | 0.1           | 3 000  | Convergência lenta; MSE final alto  |
| 2   | 4                  | 0.3           | 5 000  | Boa convergência; MSE final baixo   |
| 3   | 6                  | 0.3           | 5 000  | Melhor estabilidade e menor MSE     |
| 4   | 4                  | 0.5           | 5 000  | Oscilações iniciais; converge razoável |
| 5   | 4                  | 0.1           | 10 000 | Queda tardia do erro; similar ao Exp 2 |
| 6   | 3                  | 0.2           | 3 000  | Convergência tardia; MSE intermediário |

---

## 📈 Resultados de Convergência

Cada gráfico abaixo mostra a evolução do **MSE por época** para o experimento correspondente. As figuras estão em `./images/`.

### Experimento 1  
> `H=2, LR=0.1, Ép=3 000`
> 
(![Teste 1](https://github.com/user-attachments/assets/3c21082c-068e-4e66-9cc9-3a5f0b745840))

(![Teste 1](https://github.com/user-attachments/assets/aeac40b8-6cec-4537-b47a-aa5c2e4dce06))

### Experimento 2  
> `H=4, LR=0.3, Ép=5 000`
> 
(![Teste 2](https://github.com/user-attachments/assets/d8d60a8b-8a85-47f1-80b3-0e3f3cf57ccd))

(![Teste 2](https://github.com/user-attachments/assets/d775e76a-57a6-4e6f-9ccd-dd1deeffa2cf))

### Experimento 3  
> `H=6, LR=0.3, Ép=5 000`
> 
(![Teste 3](https://github.com/user-attachments/assets/fb16dd54-cdf1-4439-a884-2ca8a44100fe))

(![Teste 3](https://github.com/user-attachments/assets/145ba71e-5586-426a-921b-8db846f56490))


### Experimento 4  
> `H=4, LR=0.5, Ép=5 000`
> 
(![Teste 4](https://github.com/user-attachments/assets/201d099e-942c-4408-997c-8c4432e67832))

(![Teste 4](https://github.com/user-attachments/assets/130fe391-d281-4a0d-9820-222a1c182b45))

### Experimento 5  
> `H=4, LR=0.1, Ép=10 000`
> 
(![Teste 5](https://github.com/user-attachments/assets/12ea6a13-5d0a-46d9-8b07-5ffa6c5411ce))

(![Teste 5](https://github.com/user-attachments/assets/5ef9cb8e-7a3e-42d6-99ef-b54386f07524))


### Experimento 6  
> `H=3, LR=0.2, Ép=3 000`
>  
(![Teste 6](https://github.com/user-attachments/assets/b8709f3e-2fe8-4c54-bd10-6b7db388c07f))

(![Teste 6](https://github.com/user-attachments/assets/4361efd9-b5ac-4b60-8a13-aba24003368f))

---

## 🔍 Análise dos Resultados

- **Experimento 3** (`6 neurons`, `LR=0.3`): melhor **MSE final** e curva mais suave, mostrando capacidade de modelar a não‑linearidade da paridade.  
- **Experimento 2** (`4 neurons`, `LR=0.3`): também bom desempenho, mas ligeiramente acima do Exp 3 em MSE.  
- **Experimento 4** (`LR=0.5`): converge rápido após oscilações iniciais, mas não supera LR=0.3.  
- **Experimentos com LR baixo (0.1)**: exigem muito mais épocas para alcançar MSE equivalente (Exps 1 e 5).  
- **Experimento 6** (`3 neurons`): capacidade intermediária, porém não alcança a precisão das redes com 4–6 neurônios.

---

## 🏁 Conclusão

- A configuração **[6 neurônios na oculta + learning rate 0.3 + 5 000 épocas]** apresentou o melhor equilíbrio entre **rapidez de convergência** e **baixo MSE**.
- Para aplicações que exigem menor custo computacional, **4 neurônios + LR 0.3** também é uma boa escolha.

---
