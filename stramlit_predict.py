import streamlit as st
import pandas as pd
import pickle

# Carregar o modelo salvo
model = pickle.load(open('model.sav', 'rb'))

# Criar barra lateral com opções de entrada
st.sidebar.header('Insira os dados do funcionário:')
monthly_income = st.sidebar.number_input('Renda mensal', min_value=0, max_value=100000, value=5000)
age = st.sidebar.number_input('Idade', min_value=18, max_value=100, value=30)
daily_rate = st.sidebar.number_input('Taxa diária', min_value=0, max_value=1000, value=500)
years_at_company = st.sidebar.number_input('Anos na empresa', min_value=0, max_value=50, value=5)
monthly_rate = st.sidebar.number_input('Taxa mensal', min_value=0, max_value=20000, value=10000)
total_working_years = st.sidebar.number_input('Total de anos trabalhados', min_value=0, max_value=50, value=10)
employee_number = st.sidebar.number_input('Número do funcionário', min_value=0, max_value=5000, value=1000)
overtime = st.sidebar.selectbox('Trabalha horas extras?', ['Não', 'Sim'])
distance_from_home = st.sidebar.number_input('Distância de casa', min_value=0, max_value=50, value=10)
hourly_rate = st.sidebar.number_input('Taxa horária', min_value=0, max_value=100, value=50)
num_companies_worked = st.sidebar.number_input('Número de empresas trabalhadas', min_value=0, max_value=10, value=2)
years_with_curr_manager = st.sidebar.number_input('Anos com o atual gerente', min_value=0, max_value=20, value=2)

# Converter a opção de horas extras para binário (0 ou 1)
overtime_binary = 1 if overtime == 'Sim' else 0

# Criar página principal com botão de previsão
st.title('App de previsão de saída de funcionários')
st.write('Insira os dados do funcionário na barra lateral e clique no botão abaixo para fazer a previsão.')

if st.button('Prever'):
    # Criar dataframe com dados do usuário
    user_data = pd.DataFrame({
        'MonthlyIncome': monthly_income,
        'Age': age,
        'DailyRate': daily_rate,
        'YearsAtCompany': years_at_company,
        'MonthlyRate': monthly_rate,
        'TotalWorkingYears': total_working_years,
        'EmployeeNumber': employee_number,
        'OverTime': overtime_binary,
        'DistanceFromHome': distance_from_home,
        'HourlyRate': hourly_rate,
        'NumCompaniesWorked': num_companies_worked,
        'YearsWithCurrManager': years_with_curr_manager
    }, index=[0])

    # Fazer a previsão utilizando o modelo carregado
    prediction = model.predict(user_data)[0]
    
    # Exibir o resultado da previsão
    if prediction == 0:
        st.write('O funcionário provavelmente não irá sair da empresa.')
    else:
        st.write('O funcionário provavelmente irá sair da empresa.')
