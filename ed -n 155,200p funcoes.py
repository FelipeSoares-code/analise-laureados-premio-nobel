[1mdiff --cc funcoes.py[m
[1mindex b12565a,7bce3e2..0000000[m
[1m--- a/funcoes.py[m
[1m+++ b/funcoes.py[m
[36m@@@ -159,23 -159,23 +159,34 @@@[m [mdef correlPD_Nobel(laureados : pd.DataF[m
      return df[m
  [m
  def extrairPopulacao():[m
[32m++<<<<<<< HEAD[m
[32m +    indicadores = {[m
[32m +        "SP.POP.TOTL": "populacao"[m
[32m +    }[m
[32m +[m
[32m +    dfPop = wbdata.get_dataframe([m
[32m +        indicadores,[m
[32m +        date=(datetime(2013,1,1), datetime(2021,12,31)),[m
[32m +        skip_cache=True[m
[32m++=======[m
[32m+     url = ([m
[32m+         "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL"[m
[32m+         "?format=json"[m
[32m+         "&date=2013:2021"[m
[32m+         "&per_page=20000"[m
[32m++>>>>>>> 4aa1780 (extraindo população direto pela API do World Bank)[m
      )[m
  [m
[31m-     dfPop = dfPop.reset_index()[m
[32m+     resposta = requests.get(url)[m
[32m+     resposta.raise_for_status()[m
  [m
[31m-     # Extrai apenas o nome do país (string) caso venha como objeto/lista[m
[31m-     dfPop["country"] = dfPop["country"].apply([m
[31m-         lambda x: x["value"] if isinstance(x, dict)[m
[31m-         else (x[0] if isinstance(x, list) else str(x))[m
[31m-     )[m
[32m+     dados = resposta.json()[1][m
[32m+ [m
[32m+     dfPop = pd.DataFrame(dados)[m
[32m+ [m
[32m+     dfPop = dfPop[[m
[32m+         ["country", "date", "value"][m
[32m+     ][m
  [m
      dfPop.rename(columns={[m
          "country": "pais",[m
