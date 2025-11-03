# 💡 Simulador de Economia Sustentável com Biogás

O **Simulador de Economia Sustentável com Biogás** é um projeto interdisciplinar que demonstra o potencial de **redução de custos com energia convencional** por meio da utilização de **biogás** — uma fonte renovável e sustentável.  
O sistema utiliza um **simulador digital** que calcula a economia energética e financeira a partir do aproveitamento de resíduos orgânicos, mostrando como a adoção de práticas sustentáveis pode ser economicamente vantajosa.

---

## 🧭 Objetivo Geral

Demonstrar o potencial de redução de custos com energia convencional através da utilização do biogás, empregando um **simulador digital** que calcula a economia gerada a partir de resíduos orgânicos.  
O projeto busca evidenciar a **viabilidade econômica e ambiental** do biogás, promovendo conscientização sobre práticas sustentáveis.

---

## 🎯 Objetivos Específicos

- Desenvolver um **simulador digital** simples para calcular a economia gerada pelo uso do biogás;  
- Implementar estruturas de dados sobre **tipos de resíduos e seu potencial energético**;  
- Criar **requisitos funcionais**, diagramas e casos de uso;  
- Aplicar **conceitos estatísticos** para calcular médias, variações e projeções;  
- Definir um **modelo de negócio** que demonstre a viabilidade empreendedora;  
- Preparar material para **feira acadêmica**, com protótipo funcional e relatórios visuais.

---

## 🌱 Justificativa

O projeto surge da necessidade de enfrentar dois desafios:
1. O **alto custo da energia convencional**;  
2. O **desperdício de resíduos orgânicos** que poderiam ser convertidos em energia.  

Ao propor uma ferramenta acessível e educativa, o projeto incentiva práticas sustentáveis e a redução da dependência de fontes não renováveis.

---

## 🧩 Estrutura do Projeto

```
biogas-simulator/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes/
│   │   ├── users.py
│   │   ├── residues.py
│   │   ├── measurements.py
│   │   └── dashboard.py
│   ├── create_biogas_db.sql
│   └── Upxbiogas.db
│
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── services/
    │   └── App.jsx
    └── package.json
```

---

## ⚙️ Tecnologias Utilizadas

### Backend
- **Python 3.11+**
- **Flask**
- **Flask-SQLAlchemy**
- **Flask-CORS**
- **SQLite**

### Frontend
- **React (JSX)**
- **Vite / CRA**
- **Recharts**
- **Axios**
- **TailwindCSS / ShadCN UI**

---

## 🛠️ Configuração do Backend

### 1️⃣ Criar o ambiente virtual
```bash
cd backend
python -m venv venv
.env\Scriptsctivate
# ou
source venv/bin/activate
```

### 2️⃣ Instalar dependências
```bash
pip install Flask Flask-SQLAlchemy Flask-Cors
```

### 3️⃣ Criar e popular o banco de dados
```bash
sqlite3 Upxbiogas.db < create_biogas_db.sql
```

### 4️⃣ Rodar o servidor Flask
```bash
flask --debug run
```

---

## 📡 Endpoints Principais

| Método | Endpoint | Descrição |
|--------|-----------|------------|
| **GET** | `/api/users` | Lista todos os usuários |
| **POST** | `/api/users` | Cria um novo usuário |
| **GET** | `/api/residues` | Lista os tipos de resíduos |
| **POST** | `/api/measurements` | Adiciona uma medição de resíduo |
| **GET** | `/api/dashboard` | Retorna dados consolidados |

---

## 📊 Exemplo de Retorno do Dashboard

```json
{
  "overview": {
    "total_users": 4,
    "total_measurements": 7,
    "total_energy_kwh": 820.5,
    "total_savings_reais": 779.47
  },
  "ranking": [
    { "user": "Ana Silva", "total_energy_kwh": 150.0, "total_savings": 142.5 },
    { "user": "João Souza", "total_energy_kwh": 72.0, "total_savings": 68.4 }
  ],
  "by_residue": [
    { "residue": "Esterco bovino", "total_energy_kwh": 200.0, "total_savings": 190.0 },
    { "residue": "Bagaço de cana", "total_energy_kwh": 180.0, "total_savings": 171.0 }
  ]
}
```
