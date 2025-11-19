from google import genai
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
hyper_secret_token = open("../fila.txt", 'r')
tokin = hyper_secret_token.read()



engine = create_engine('sqlite:///discord_chat_log.db')  
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

true, false = True, False


class Chat_log(Base):
    __tablename__ = 'historial'
    id= Column(Integer, primary_key=true)
    user = Column(String(32), nullable=false)
    question = Column(String(2000), nullable=false)
    answer = Column(String(2000), nullable=false)



client = genai.Client(api_key=f"{tokin}")
#Base.metadata.create_all(engine)
def responde_gemini(que_cosa, quien):  
    try:
        historial = db_session.query(Chat_log).filter_by(user=quien).all()
        strial = "Este es el historial de la conversacion, usalo como referencia hasta que se indique que parte es la nueva pregunta."
        for item in historial:
            strial = strial + f" esto pregunto: {item.question}"
            strial = strial + f" esto respondiste: {item.answer}"
        que_cosa = strial + f" Esta la pregunta nueva: {que_cosa}"
    except Exception as E:
        print(E) #Si no esta roto no lo arregles, verdad? 
    returnable = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=que_cosa,
    )

    nuevo_log = Chat_log(question=que_cosa, answer=returnable, user=quien) 
    db_session.add(nuevo_log)
    db_session.commit()


    return returnable
