import json
from portfolio.models import TFC

with open('ficheiro.json', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    TFC.objects.create(
        titulo=item.get('titulo', '')[:100],
        descricao=item.get('sumario', ''),
        rating=item.get('Rating', 0),
        autores=item.get('autor(es)', '')[:200],
        orientadores=item.get('orientador', '')[:200],
        tecnologias=item.get('Tecnologias usadas', '')[:200],
        areas=item.get('Áreas', '')[:200],
        keyWords=item.get('Palavras chave', '')[:200],
        pdf=item.get('pdf', ''),
        imagem=item.get('imagem', ''),
    )

print("Import concluído")