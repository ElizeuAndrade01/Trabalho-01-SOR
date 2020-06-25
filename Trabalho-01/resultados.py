
def resultadoM (person_age, age_i, person_height, person_weight, peso_minimo, peso_ideal, peso_max, alt_min, alt_ideal, alt_max):
  if person_age == age_i:
    if person_weight >= peso_minimo and person_weight < peso_ideal:
      weight_result = print("O peso do seu Filho é Minimo")
    elif ( person_weight >= peso_ideal and person_weight < peso_max ):
      weight_result = print("O peso do seu Filho é Ideal.")
    elif ( person_weight >= peso_max):
      weight_result = print("O peso do seu Filho é Máximo.")
    else:
      weight_result = print("O peso do seu Filho é Abaixo do Minimo, procure ajuda médica.")

    if ( person_height >= alt_min and person_height < alt_ideal ):
      height_result = print("A altura do seu Filho é Minima")
    elif ( person_height >= alt_ideal and person_height < alt_max ):
      height_result = print("A altura do seu Filho é Ideal.")
    elif ( person_height >= alt_max):
      height_result = print("A altura do seu Filho é Máxima.")
    else:
      height_result = print("A altura do seu Filho é Abaixo da Minima.")

    return(weight_result, height_result)
  else:
    return


def resultadoF (person_age, age_i, person_height, person_weight, peso_minimo, peso_ideal, peso_max, alt_min, alt_ideal, alt_max):
  if person_age == age_i:
    if person_weight >= peso_minimo and person_weight < peso_ideal:
      weight_result = print("O peso da seu Filha é Minimo")
    elif ( person_weight >= peso_ideal and person_weight < peso_max ):
      weight_result = print("O peso da seu Filha é Ideal.")
    elif ( person_weight >= peso_max):
      weight_result = print("O peso da seu Filha é Máximo.")
    else:
      weight_result = print("O peso da seu Filha é Abaixo do Minimo, procure ajuda médica.")

    if ( person_height >= alt_min and person_height < alt_ideal ):
      height_result = print("A altura da seu Filha é Minima")
    elif ( person_height >= alt_ideal and person_height < alt_max ):
      height_result = print("A altura da seu Filha é Ideal.")
    elif ( person_height >= alt_max):
      height_result = print("A altura da seu Filha é Máxima.")
    else:
      height_result = print("A altura da seu Filha é Abaixo da Minima.")

    return(weight_result, height_result)
  else:
    return


    