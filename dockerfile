FROM python:3.8
EXPOSE 8501
#EXPOSE 80
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run app.py
## streamlit uses port 8501 by default, so need to remap to 80
#CMD streamlit run app.py --server.port 80

