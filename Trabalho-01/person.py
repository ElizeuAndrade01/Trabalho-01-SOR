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

    result = resultados.resultado

    #Tabelas por idade:
    #MASCULINA:
    result(self.person_age, 3, self.person_height, self.person_weight, 12.25, 14.61, 17.78, 90.6, 96.2, 102.8)
    result(self.person_age, 4, self.person_height, self.person_weight, 13.65, 16.51, 20.09, 97.5, 103.4, 110.4)
    result(self.person_age, 5, self.person_height, self.person_weight, 15.24, 18.37, 22.86, 102, 108.7, 117.1)
    result(self.person_age, 6, self.person_height, self.person_weight, 17.46, 21.51, 27.71, 108.5, 117.5, 126.2)
    result(self.person_age, 7, self.person_height, self.person_weight, 19.50, 24.54, 31.71, 114, 124.1, 133.4)
    result(self.person_age, 8, self.person_height, self.person_weight, 21.77, 27.26, 36.02, 119.6, 130, 140.2)
    result(self.person_age, 9, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)
    result(self.person_age, 10, self.person_height, self.person_weight, 25.76, 32.61, 45.36, 128.7, 140.3, 150.3)
    result(self.person_age, 11, self.person_height, self.person_weight, 28.03, 35.20, 50.67, 133.4, 144.2, 154.4)
    result(self.person_age, 12, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)
    result(self.person_age, 13, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)
    result(self.person_age, 14, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)
    result(self.person_age, 15, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)
    result(self.person_age, 16, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)
    result(self.person_age, 17, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)
    result(self.person_age, 18, self.person_height, self.person_weight, 23.81, 29.94, 40.73, 124.2, 135.5, 145.3)

teste = person("M", 4, 16.2, 92.3)

teste.resultado()