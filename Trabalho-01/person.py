import resultados

class person:
  def __init__(self, gender, age, weight, height):
    self.person_gender = gender
    self.person_age = age
    self.person_weight = weight
    self.person_height = height

  


  def resultado(self):
    
    #Variaveis Resultado
    

    
    #if(self.person_gender = M):
    #  if(self.person_age = 3):
    #    if ( self.person_weight >= 12.25 and self.person_weight < 14.61 ):
    #      weight_result = print("O peso do seu Filho é Minimo")
    #    elif ( self.person_weight >= 14.61 and self.person_weight < 17.78 ):
    #      weight_result = print("O peso do seu Filho é Ideal.")
    #    elif ( self.person_weight >= 17.78):
    #      weight_result = print("O peso do seu Filho é Máximo.")
    #    else:
    #      weight_result = print("O peso do seu Filho é Abaixo do Minimo, procure ajuda médica.")
    #
    #    if ( self.person_height >= 90.6 and self.person_height < 96.2 ):
    #      height_result = print("A altura do seu Filho é Minima")
    #    elif ( self.person_height >= 96.2 and self.person_height < 102.8 ):
    #      height_result = print("A altura do seu Filho é Ideal.")
    #    elif ( self.person_height >= 102.8):
    #      height_result = print("A altura do seu Filho é Máxima.")
    #    else:
    #      height_result = print("A altura do seu Filho é Abaixo da Minima, procure ajuda médica.")
    
    #resultado (self, person_age, age_index, person_height, person_weight, peso_minimo,
    #peso_ideal, peso_max,alt_min, alt_ideal, alt_max, weight_result, height_result)

    result = resultados.resultadoM
    resultF = resultados.resultadoF

    #Tabelas por idade:
    #MASCULINA:
    if self.person_gender == "M":
      result(self.person_age, 3, self.person_height, self.person_weight, 12.25, 14.61, 17.78, 90.6, 96.2, 102.8)
      result(self.person_age, 4, self.person_height, self.person_weight, 13.65, 16.51, 20.09, 97.5, 103.4, 110.4)
      result(self.person_age, 5, self.person_height, self.person_weight, 15.24, 18.37, 22.86, 102, 108.7, 117.1)
      result(self.person_age, 6, self.person_height, self.person_weight, 17.46, 21.51, 27.71, 108.5, 117.5, 126.2)
      result(self.person_age, 7, self.person_height, self.person_weight, 19.50, 24.54, 31.71, 114, 124.1, 133.4)
      result(self.person_age, 8, self.person_height, self.person_weight, 21.77, 27.26, 36.02, 119.6, 130, 140.2)
      result(self.person_age, 9, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)
      result(self.person_age, 10, self.person_height, self.person_weight, 25.76, 32.61, 45.36, 128.7, 140.3, 150.3)
      result(self.person_age, 11, self.person_height, self.person_weight, 28.03, 35.20, 50.67, 133.4, 144.2, 154.4)
      result(self.person_age, 12, self.person_height, self.person_weight, 30.48, 38.28, 56.34, 138.1, 149.6, 161.9)
      result(self.person_age, 13, self.person_height, self.person_weight, 32.66, 42.18, 62.60, 142.2, 155, 169.5)
      result(self.person_age, 14, self.person_height, self.person_weight, 36.20, 48.81, 68.31, 146.4, 162.7, 177.1)
      result(self.person_age, 15, self.person_height, self.person_weight, 41.41, 54.48, 73.30, 151.7, 167.8, 181.8)
      result(self.person_age, 16, self.person_height, self.person_weight, 46.90, 58.83, 77.34, 156.5, 171.6, 185.6)
      result(self.person_age, 17, self.person_height, self.person_weight, 50.12, 61.78, 79.65, 159, 173.7, 186.6)
      result(self.person_age, 18, self.person_height, self.person_weight, 51.26, 63.05, 81.19, 159.6, 174.5, 187.6)
    elif self.person_gender == "F":
      resultF(self.person_age, 3, self.person_height, self.person_weight, 11.61, 14.42, 18.96, 88.4, 95.7, 103.5)
      resultF(self.person_age, 4, self.person_height, self.person_weight, 13.25, 16.42, 21.86, 95.2, 103.2, 112.3)
      resultF(self.person_age, 5, self.person_height, self.person_weight, 14.56, 18.37, 23.95, 100, 109.1, 118.8)
      resultF(self.person_age, 6, self.person_height, self.person_weight, 16.87, 21.09, 26.63, 108, 115.9, 125.4)
      resultF(self.person_age, 7, self.person_height, self.person_weight, 18.73, 23.68, 30.63, 114, 122.3, 131.4)
      resultF(self.person_age, 8, self.person_height, self.person_weight, 20.55, 26.35, 35.79, 119.1, 128, 137.4)
      resultF(self.person_age, 9, self.person_height, self.person_weight, 22.27, 28.94, 40.78, 123.6, 132.9, 143.4)
      resultF(self.person_age, 10, self.person_height, self.person_weight, 24.13, 31.89, 46.22, 127.7, 138.6, 149.3)
      resultF(self.person_age, 11, self.person_height, self.person_weight, 26.26, 35.74, 51.21, 132.3, 144.7, 157.4)
      resultF(self.person_age, 12, self.person_height, self.person_weight, 28.85, 39.74, 57.92, 137.8, 151.9, 164.6)
      resultF(self.person_age, 13, self.person_height, self.person_weight, 32.75, 44.95, 64.55, 143.7, 157.1, 168.4)
      resultF(self.person_age, 14, self.person_height, self.person_weight, 37.69, 49.17, 68.40, 148.2, 159.6, 170.7)
      resultF(self.person_age, 15, self.person_height, self.person_weight, 40.37, 51.48, 70.40, 150.2, 161.1, 171.6)
      resultF(self.person_age, 16, self.person_height, self.person_weight, 41.64, 53.07, 71.53, 150.8, 162.2, 172)
      resultF(self.person_age, 17, self.person_height, self.person_weight, 42.59, 54.02, 72.35, 151, 162.5, 172.2)
      resultF(self.person_age, 18, self.person_height, self.person_weight, 42.87, 54.39, 72.69, 151, 162.5, 172.2)
    else:
      print("Insira um caractere valido")

    teste = person('M', 10, 35.2, 150.2)

    teste.resultado()



