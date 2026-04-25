@echo off
title J.A.R.V.I.S. - Console de Operação
:: Entra no ambiente virtual
call .venv\Scripts\activate
:: Roda o script principal
python main.py
:: Se o programa fechar, mantém a janela aberta para você ver erros
pause