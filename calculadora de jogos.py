from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import pickle,os,time,subprocess
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.FirefoxOptions()
options.add_argument("-headless")
url_parcial = "https://www.premierleague.com/clubs"
temporada = "/stats?co=1&se=719"
salts ="\n"
time1= ''
time2= ''
goals1 = 1
goals2 = 4

url=["/1/Arsenal",
     "/26/Leicester-City",
     "/4/Chelsea",
     "/2/Aston-Villa",
     "/127/Bournemouth",
     "/130/Brentford",
     "/131/Brighton-and-Hove-Albion",
     "/43/Burnley",
     "/6/Crystal-Palace",
     "/7/Everton",
     "/34/Fulham",
     "/10/Liverpool",
     "163/Luton-Town/",
     "/11/Manchester-City",
     "/12/Manchester-United",
     "/23/Newcastle-United",
     "/15/Nottingham-Forest",
     "/18/Sheffield-United",
     "/21/Tottenham-Hotspur/",
     "/25/West-Ham-United",
     "/38/Wolverhampton-Wanderers",
     "/20/Southampton"]

lista = ["arsenal           ",
         "Leicester-City    ",
         "chelsea           ",
         "Aston-Villa       ",
         "Bournemouth       ",
         "Brentford         ",
         "Brighton          ",
         "Burnley           ",
         "Crystal-Palace    ",
         "Everton           ",
         "Fulham            ",
         "Liverpool         ",
         "Luton-Town        ",
         "Manchester-City   ",
         "Manchester-United ",
         "Newcastle-United  ",
         "Nottingham-Forest ",
         "Sheffield-United  ",
         "Tottenham         ",
         "West-Ham          ",
         "Wolverhampton     ",
         "Southampton       "]

class web_drivers:   
    def prints():
        print('')
    def nomes():
        times=str(driver.title)
        times= times.replace("Statistics | Premier League",'')
        #print(time2)
        return (times)
    
    def savefille():
     os.chdir('/home/cristian-pc/Documentos/bot')   
     times_a_jogar = pd.DataFrame({ 
        'nomes' : ["partidas jogadas","vitorias","percas","gols","gols concedidos","jogos sem perder",
                  "Goals","gols por partida","chutes","chutes no alvo","penaltis","chances de gol","acertou na trave",
                  "passes","passes por partida","crusamentos",
                  "jogos sem perder","gols concedidos","gols concedidos por partida","Saves","recuperação de bolas","chetes bloqueados",
                  "Interceptações","folgas","duelos que possui","erros que levaram a gol","possui gols",                                     
                  ],
        str(time1): [
        str(resultados1[0]),str(resultados1[1]),str(resultados1[2]),
        str(resultados1[3]),str(resultados1[4]),str(resultados1[5]),
        str(resultados1[6]),str(resultados1[7]),str(resultados1[8]),
        str(resultados1[9]),str(resultados1[10]),str(resultados1[11]),
        str(resultados1[12]),str(resultados1[13]),str(resultados1[14]),
        str(resultados1[15]),str(resultados1[16]),str(resultados1[17]),
        str(resultados1[18]),str(resultados1[19]),str(resultados1[20]),
        str(resultados1[21]),str(resultados1[22]),str(resultados1[23]),
        str(resultados1[24]),str(resultados1[25]),str(resultados1[26]),
        ],
        str(time2): [
        str(resultados2[0]),str(resultados2[1]),str(resultados2[2]),
        str(resultados2[3]),str(resultados2[4]),str(resultados2[5]),
        str(resultados2[6]),str(resultados2[7]),str(resultados2[8]),
        str(resultados2[9]),str(resultados2[10]),str(resultados2[11]),
        str(resultados2[12]),str(resultados2[13]),str(resultados2[14]),
        str(resultados2[15]),str(resultados2[16]),str(resultados2[17]),
        str(resultados2[18]),str(resultados2[19]),str(resultados2[20]),
        str(resultados2[21]),str(resultados2[22]),str(resultados2[23]),
        str(resultados2[24]),str(resultados2[25]),str(resultados2[26]),
        ],
        "=B1": [   
        "=sum(B2/C2)",'=sum(B3/C3)','=sum(B4/C4)','=sum(B5/C5)',
        "=sum(B6/C6)",'=sum(B7/C7)','=sum(B8/C8)','=sum(B9/C9)',
        "=sum(B10/C10)",'=sum(B11/C11)','=sum(B12/C12)','=sum(B13/C13)',
        "=sum(B14/C14)",'=sum(B15/C15)','=sum(B16/C16)','=sum(B17/C17)',
        "=sum(B18/C18)",'=sum(B19/C19)','=sum(B20/C20)','=sum(B21/C21)',
        "=sum(B22/C22)",'=sum(B23/C23)','=sum(B24/C24)','=sum(B25/C25)',                          
        '=sum(B26/C26)','=sum(B27/C27)', '=IFERROR(B28/C28;"0")',],
                                    
        '=C1': [   
        "=sum(C2/B2)",'=sum(C3/B3)','=sum(C4/B4)','=sum(C5/B5)',
        "=sum(C6/B6)",'=sum(C7/B7)','=sum(C8/B8)','=sum(C9/B9)',
        "=sum(C10/B10)",'=sum(C11/B11)','=sum(C12/B12)','=sum(C13/B13)',
        "=sum(C14/B14)",'=sum(C15/B15)','=sum(C16/B16)','=sum(C17/B17)',
        "=sum(C18/B18)",'=sum(C19/B19)','=sum(C20/B20)','=sum(C21/B21)',
        "=sum(C22/B22)",'=sum(C23/B23)','=sum(C24/B24)','=sum(C25/B25)',
        "=sum(C26/B26)",'=sum(C27/B27)', '=IFERROR(C28/B28;"0")',], 
        
        '': [   
        "diferença de percas e vitorias",'chances de bloqueio de gol','chances de criar gol','chances de golear',
        "",'','','',
        "",'','','',
        "",'','','',
        "",'','','',
        "",'','','', 
        "",'','',], 
               
        '=B1 ' : [
        "=SUM((B3/B4)/10)",'=SUM(((B23/C24)*B11)/100)','=SUM(((B11/B13)*(B8/100)*B9))','=SUM((G4/H3)/10)',
        "",'','','',
        "",'','','',
        "",'','','',
        "",'','','',
        "",'','','', 
        "",'','',],    
             
        '=C1 ' : [
        '=SUM((C3/C4)/10)','=SUM(((C23/B24)*C11)/100)','=SUM(((C11/C13)*(C8/100)*C9))','=SUM((H4/H3)/10)',
        "",'','','',
        "",'','','',
        "",'','','',
        "",'','','',
        "",'','','', 
        "",'','',],           
        })
     
     file_name = str(time1)+"x "+str(time2)+'.xlsx'
     times_a_jogar.to_excel(file_name, index=False)

     print(str(file_name)," salvo")
           
    def times():
        i = 0
        while i in range (0,22):
         print(lista[i],lista.index(lista[int(i)]))
         i = i + 1         
        
    def get_elements():
        #menu superios
        mplay =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/div/div[1]/div[2]/span').text
        wins =    driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/div/div[2]/div[2]/span').text
        lossers = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/div/div[3]/div[2]/span').text
        goals =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/div/div[4]/div[2]/span').text
        goalsconcept =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/div/div[5]/div[2]/span').text
        clsheets = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/div/div[6]/div[2]/span').text
        #menu atack
        Goals =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[1]/div/div[2]/span[2]/span').text
        Gpmatch = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[1]/div/div[3]/span[2]/span').text
        shots =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[1]/div/div[4]/span[2]/span').text
        shotsontargt = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[1]/div/div[5]/span[2]/span').text
        penaltis =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[1]/div/div[7]/span[2]/span').text
        gchance = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[1]/div/div[8]/span[2]/span').text
        hitwood =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[1]/div/div[9]/span[2]/span').text
        #menu team play
        passes = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[2]/div/div[2]/span[2]/span').text
        passespmat =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[2]/div/div[3]/span[2]/span').text
        crosses = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[2]/div/div[5]/span[2]/span').text
        #menu defesa
        cleanshets =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[2]/span[2]/span').text
        goalsconced = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[3]/span[2]/span').text
        goalsconcedpmat =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[4]/span[2]').text
        Saves = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[5]/span[2]/span').text
        Tackles =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[6]/span[2]/span').text
        Blockedshots = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[8]/span[2]/span').text
        Interceptions =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[9]/span[2]').text
        Clearances = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[10]/span[2]/span').text
        Duels_Won  =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[12]/span[2]/span').text
        errortogoal = driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[13]/span[2]/span').text
        own_goals =   driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/ul/li[3]/div/div[14]/span[2]/span').text
        return (mplay,wins,lossers,goals,goalsconcept,clsheets,
               Goals,Gpmatch,shots,shotsontargt,penaltis,gchance,hitwood,
               passes,passespmat,crosses,
               cleanshets,goalsconced,goalsconcedpmat,Saves,Tackles,Blockedshots,
               Interceptions,Clearances,Duels_Won,errortogoal,own_goals)
   
    def cookie():
        if os.path.exists('cookies.pkl'):
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                 driver.add_cookie(cookie)
            driver.refresh()
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        
    def abrirgecko1():
        driver.get(str(url_parcial)+str(url1)+str(temporada))

    def abrirgecko2():
        driver.get(str(url_parcial)+str(url2)+str(temporada))

if __name__ == '__main__':
 web_drivers.times()
 inputs = input("escolha o time:")
 inputs2 = input("escolha o time:")
 driver = webdriver.Firefox(options=options)
 url1 = url[int(inputs)]
 web_drivers.abrirgecko1()
 time1 =  web_drivers.nomes()
 web_drivers.cookie()
 time.sleep(2)
 web_drivers.get_elements()
 resultados1= web_drivers.get_elements()
 #print(str(resultados1))

 driver = webdriver.Firefox(options=options)
 url2 = url[int(inputs2)]
 web_drivers.abrirgecko2()
 time2 = web_drivers.nomes()
 web_drivers.cookie()
 time.sleep(2)
 web_drivers.get_elements()
 resultados2= web_drivers.get_elements()
 #print(str(resultados2))
 web_drivers.savefille()
 subprocess.run("pkill firef*", shell=True, check=True)
