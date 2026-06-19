import funcoes as fn

def nacionalidades():
    nacionalidades = fn.dfNacionalidades()

    # Index(['Id', 'Firstname', 'Surname', 'Born', 'Died', 'Born country',
    #    'Born country code', 'Born city', 'Died country', 'Died country code',
    #    'Died city', 'Gender', 'Year', 'Category', 'Overall motivation',
    #    'Motivation', 'Organization name', 'Organization city',
    #    'Organization country', 'Geo Shape', 'Geo Point 2D'],
    #   dtype='str')

    nacionalidades.drop(
        [
            'Born city','Died city',
            'Overall motivation', 'Motivation',
            'Organization city', 'Geo Shape', 'Geo Point 2D'
        ],
        axis='columns', inplace=True
    )

    nacionalidades.rename(columns={
        "Id" : "id",
        "Firstname" : "nome",
        "Surname" : "sobrenome",
        "Born" : "nascimento",
        "Died" : "morte",
        "Born country" : "pais_nasc",
        "Born country code" : "cod_pais_nasc",
        "Died country" : "pais_morte",
        "Died country code" : "cod_pais_morte",
        "Gender" : "genero",
        "Year" : "ano_venc",
        "Category" : "categoria",
        "Organization name" : "nome_org",
        "Organization country" : "pais_org"
    }, inplace=True)

    return nacionalidades